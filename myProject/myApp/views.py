from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Sum
from .models import Flight, Ticket, Package, Deal, Profile, PackageBooking, DealBooking
from .countries import COUNTRIES_WITH_CODES
import qrcode
import base64
from io import BytesIO
from datetime import datetime


def index(request):
    flights = Flight.objects.all()[:6]
    packages = Package.objects.all()[:3]
    deals = Deal.objects.filter(is_active=True)[:3]
    
    # Search functionality from homepage
    if request.GET.get('destination') or request.GET.get('date'):
        return redirect('flights')
    
    return render(request, 'index.html', {
        'flights': flights,
        'packages': packages,
        'deals': deals
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, "Please provide both username and password")
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('index')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        
        # Validation
        if not username or not email or not password or not confirm:
            messages.error(request, "All fields are required")
            return redirect('signup')
        
        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=user)
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
        except Exception as e:
            messages.error(request, "An error occurred. Please try again.")
            return redirect('signup')
    
    return render(request, 'signup.html')


def flights_view(request):
    flights = Flight.objects.all()
    
    # Search and filter
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')
    airline = request.GET.get('airline', '')
    max_price = request.GET.get('max_price', '')
    flight_type = request.GET.get('flight_type', '')
    
    if destination:
        flights = flights.filter(Q(destination__icontains=destination) | Q(origin__icontains=destination))
    if date:
        flights = flights.filter(departure_date=date)
    if airline:
        flights = flights.filter(airline__icontains=airline)
    if max_price:
        try:
            flights = flights.filter(price__lte=float(max_price))
        except ValueError:
            pass
    if flight_type:
        flights = flights.filter(flight_type=flight_type)
    
    # Get unique values for dropdowns
    destinations = Flight.objects.values_list('destination', flat=True).distinct().order_by('destination')
    airlines = Flight.objects.values_list('airline', flat=True).distinct().order_by('airline')
    
    return render(request, 'flights.html', {
        'flights': flights,
        'destinations': destinations,
        'airlines': airlines,
    })


def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if flight.is_fully_booked():
        messages.error(request, "Sorry, all seats are booked for this flight. Please choose another flight.")
        return redirect('flights')
    
    booked_seats = flight.get_booked_seats()
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")
        seat_numbers = request.POST.get("seat_numbers", "")
        seat_class = request.POST.get("seat_class", "economy")
        passport = request.POST.get("passport", "")
        nationality = request.POST.get("nationality", "")
        special_requests = request.POST.get("special_requests", "")
        num_passengers = int(request.POST.get("num_passengers", 1))
        
        if not name or not email or not seat_numbers:
            messages.error(request, "Name, email, and seat selection are required")
            return redirect('book_flight', flight_id=flight_id)
        
        selected_seats = [s.strip() for s in seat_numbers.split(',')]
        
        if len(selected_seats) != num_passengers:
            messages.error(request, f"Please select {num_passengers} seat(s)")
            return redirect('book_flight', flight_id=flight_id)
        
        for seat in selected_seats:
            if seat in booked_seats:
                messages.error(request, f"Seat {seat} is already booked")
                return redirect('book_flight', flight_id=flight_id)
        
        if num_passengers > flight.seats_available:
            messages.error(request, f"Only {flight.seats_available} seats available")
            return redirect('book_flight', flight_id=flight_id)
        
        try:
            ticket = Ticket.objects.create(
                user=request.user if request.user.is_authenticated else None,
                passenger_name=name,
                email=email,
                phone=phone,
                flight=flight,
                seat_number=seat_numbers,
                seat_class=seat_class,
                passport_number=passport,
                nationality=nationality,
                special_requests=special_requests,
                num_passengers=num_passengers,
                status='confirmed',
                payment_status=True
            )
            
            flight.seats_available -= num_passengers
            flight.save()
            
            qr_code = generate_qr(ticket)
            
            messages.success(request, f"Flight booked successfully for {num_passengers} passenger(s)! Seats: {seat_numbers}")
            return render(request, "ticket_overview.html", {
                "ticket": ticket,
                "qr_code": qr_code
            })
        except Exception as e:
            messages.error(request, f"Booking failed: {str(e)}")
            return redirect('book_flight', flight_id=flight_id)
    
    return render(request, "book_flight.html", {
        "flight": flight,
        "booked_seats": booked_seats,
        "countries": COUNTRIES_WITH_CODES
    })


def generate_qr(ticket):
    qr_data = f"""Ticket ID: {ticket.ticket_id}
Name: {ticket.passenger_name}
Flight: {ticket.flight.flight_number}
From: {ticket.flight.origin}
To: {ticket.flight.destination}
Date: {ticket.flight.departure_date}
Time: {ticket.flight.departure_time}"""
    
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return qr_base64


def packages_view(request):
    packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': packages})


def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        travelers = request.POST.get("travelers", 1)
        
        if not name or not email or not phone:
            messages.error(request, "All fields are required")
            return redirect('book_package', package_id=package_id)
        
        try:
            booking = PackageBooking.objects.create(
                user=request.user if request.user.is_authenticated else None,
                package=package,
                customer_name=name,
                email=email,
                phone=phone,
                travelers=int(travelers),
                status='confirmed'
            )
            
            messages.success(request, "Package booked successfully!")
            return redirect('profile' if request.user.is_authenticated else 'index')
        except Exception as e:
            messages.error(request, "Booking failed. Please try again.")
            return redirect('book_package', package_id=package_id)
    
    return render(request, "book_package.html", {"package": package})


def deals_view(request):
    deals = Deal.objects.filter(is_active=True)
    return render(request, 'deals.html', {'deals': deals})


def book_deal(request, deal_id):
    deal = get_object_or_404(Deal, id=deal_id)
    
    if not deal.is_active:
        messages.error(request, "This deal is no longer active")
        return redirect('deals')
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        
        if not name or not email or not phone:
            messages.error(request, "All fields are required")
            return redirect('book_deal', deal_id=deal_id)
        
        try:
            booking = DealBooking.objects.create(
                user=request.user if request.user.is_authenticated else None,
                deal=deal,
                customer_name=name,
                email=email,
                phone=phone,
                status='confirmed'
            )
            
            messages.success(request, "Deal booked successfully!")
            return redirect('profile' if request.user.is_authenticated else 'index')
        except Exception as e:
            messages.error(request, "Booking failed. Please try again.")
            return redirect('book_deal', deal_id=deal_id)
    
    return render(request, "book_deal.html", {"deal": deal})


def autocomplete_destinations(request):
    query = request.GET.get('q', '')
    if query:
        destinations = Flight.objects.filter(
            Q(destination__icontains=query) | Q(origin__icontains=query)
        ).values_list('destination', flat=True).distinct()[:10]
        return JsonResponse(list(destinations), safe=False)
    return JsonResponse([], safe=False)


def autocomplete_airlines(request):
    query = request.GET.get('q', '')
    if query:
        airlines = Flight.objects.filter(
            airline__icontains=query
        ).values_list('airline', flat=True).distinct()[:10]
        return JsonResponse(list(airlines), safe=False)
    return JsonResponse([], safe=False)


@login_required
def request_refund(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id, user=request.user)
    
    if ticket.status == 'refunded':
        messages.error(request, "This ticket has already been refunded")
        return redirect('profile')
    
    if ticket.status == 'cancelled':
        messages.error(request, "This ticket has already been cancelled")
        return redirect('profile')
    
    if request.method == "POST":
        from datetime import datetime, timezone
        
        # Calculate refund amount (80% of ticket price - 20% cancellation fee)
        refund_amount = ticket.calculate_refund_amount()
        
        # Update ticket status
        ticket.status = 'refunded'
        ticket.refund_requested_at = datetime.now(timezone.utc)
        ticket.refund_amount = refund_amount
        ticket.refund_processed = True
        ticket.save()
        
        # Return seat to available pool
        ticket.flight.seats_available += 1
        ticket.flight.save()
        
        messages.success(request, f"Refund processed successfully! Amount: ${refund_amount:.2f} (20% cancellation fee deducted)")
        return redirect('profile')
    
    refund_amount = ticket.calculate_refund_amount()
    cancellation_fee = float(ticket.flight.price) * 0.20 if ticket.flight.price else 0
    
    return render(request, 'refund_request.html', {
        'ticket': ticket,
        'refund_amount': refund_amount,
        'cancellation_fee': cancellation_fee
    })


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    # Allow access if user owns the ticket or is staff
    if ticket.user != request.user and not request.user.is_staff:
        messages.error(request, "You don't have permission to view this ticket")
        return redirect('profile')
    
    qr_code = generate_qr(ticket)
    
    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'qr_code': qr_code
    })


@login_required
def package_detail(request, booking_id):
    booking = get_object_or_404(PackageBooking, booking_id=booking_id)
    
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, "You don't have permission to view this booking")
        return redirect('profile')
    
    return render(request, 'package_detail.html', {'booking': booking})


@login_required
def deal_detail(request, booking_id):
    booking = get_object_or_404(DealBooking, booking_id=booking_id)
    
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, "You don't have permission to view this booking")
        return redirect('profile')
    
    return render(request, 'deal_detail.html', {'booking': booking})


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    tickets = Ticket.objects.filter(user=request.user).order_by('-booked_at')
    package_bookings = PackageBooking.objects.filter(user=request.user).order_by('-booked_at')
    deal_bookings = DealBooking.objects.filter(user=request.user).order_by('-booked_at')
    
    return render(request, 'profile.html', {
        'profile': profile, 
        'tickets': tickets,
        'package_bookings': package_bookings,
        'deal_bookings': deal_bookings
    })


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        profile.phone = request.POST.get('phone', '')
        profile.address = request.POST.get('address', '')
        
        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']
        
        profile.save()
        messages.success(request, "Profile updated successfully")
        return redirect('profile')
    
    return render(request, 'edit_profile.html', {'profile': profile})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, "Access denied. Admin privileges required.")
        return redirect('index')
    
    total_bookings = Ticket.objects.count()
    total_flights = Flight.objects.count()
    total_packages = Package.objects.count()
    total_deals = Deal.objects.filter(is_active=True).count()
    
    # Calculate total revenue
    flight_revenue = Ticket.objects.filter(payment_status=True).aggregate(
        total=Sum('flight__price'))['total'] or 0
    package_revenue = PackageBooking.objects.aggregate(
        total=Sum('package__price'))['total'] or 0
    deal_revenue = DealBooking.objects.aggregate(
        total=Sum('deal__discounted_price'))['total'] or 0
    total_revenue = flight_revenue + package_revenue + deal_revenue
    
    recent_bookings = Ticket.objects.all().order_by('-booked_at')[:10]
    popular_destinations = Flight.objects.values('destination').annotate(count=Count('ticket')).order_by('-count')[:5]
    
    context = {
        'total_bookings': total_bookings,
        'total_flights': total_flights,
        'total_packages': total_packages,
        'total_deals': total_deals,
        'total_revenue': total_revenue,
        'recent_bookings': recent_bookings,
        'popular_destinations': popular_destinations,
    }
    
    return render(request, 'admin_dashboard.html', context)
