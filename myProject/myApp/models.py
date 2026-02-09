from django.contrib.auth.models import User
from django.db import models
import uuid

class Flight(models.Model):
    FLIGHT_TYPE_CHOICES = [
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ]
    
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=50)
    flight_type = models.CharField(max_length=20, choices=FLIGHT_TYPE_CHOICES, default='international')

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    departure_time = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)

    departure_date = models.DateField(null=True, blank=True)

    duration = models.CharField(max_length=50, null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    seats_available = models.IntegerField(default=100)
    total_seats = models.IntegerField(default=100)
    aircraft_type = models.CharField(max_length=100, default="Boeing 737")
    baggage_allowance = models.CharField(max_length=50, default="20kg")

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"
    
    def get_booked_seats(self):
        booked = []
        for ticket in Ticket.objects.filter(flight=self, status__in=['confirmed', 'pending']):
            seats = ticket.seat_number.split(',')
            booked.extend([s.strip() for s in seats])
        return booked
    
    def is_fully_booked(self):
        return self.seats_available <= 0


class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='packages/', blank=True)
    includes = models.TextField(help_text="Comma-separated list")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PackageBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    travelers = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Package Booking {self.booking_id}"


class Deal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField()
    image = models.ImageField(upload_to='deals/', blank=True)
    valid_until = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class DealBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deal Booking {self.booking_id}"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    seat_class = models.CharField(max_length=20, choices=[('economy', 'Economy'), ('business', 'Business'), ('first', 'First Class')], default='economy')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.BooleanField(default=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    refund_requested_at = models.DateTimeField(null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    refund_processed = models.BooleanField(default=False)
    
    # Additional passenger details
    passport_number = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    special_requests = models.TextField(blank=True)
    num_passengers = models.IntegerField(default=1)

    def __str__(self):
        return f"Ticket {self.ticket_id}"
    
    def calculate_refund_amount(self):
        """Calculate refund with 20% cancellation fee"""
        if self.flight.price:
            return float(self.flight.price) * 0.80 * self.num_passengers
        return 0


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
