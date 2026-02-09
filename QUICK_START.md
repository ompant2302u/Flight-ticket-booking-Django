# Quick Start Guide - Updated Flight Booking System

## 🚀 Getting Started

### Step 1: Apply Database Migrations
```bash
cd "/mnt/c/Users/rajju/OneDrive/Pictures/Django project/myProject"
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Update Existing Flight Data (Optional but Recommended)
Open Django shell:
```bash
python manage.py shell
```

Run this code to update existing flights:
```python
from myApp.models import Flight

# Update all flights with default values
Flight.objects.all().update(
    total_seats=100,
    aircraft_type='Boeing 737',
    baggage_allowance='20kg'
)

# Verify
for flight in Flight.objects.all():
    print(f"{flight.flight_number}: {flight.seats_available}/{flight.total_seats} seats")

exit()
```

### Step 3: Start the Server
```bash
python manage.py runserver
```

### Step 4: Access the Application
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🧪 Testing the New Features

### Test Seat Selection
1. Go to Flights page
2. Click "Book Now" on any flight
3. Scroll to seat map
4. Click on a green (available) seat
5. Fill in passenger details
6. Submit booking
7. Verify seat number appears in ticket

### Test Refund System
1. Login to your account
2. Go to Profile page
3. Find a confirmed ticket
4. Click "Request Refund"
5. Review refund amount (80% of price)
6. Confirm refund
7. Check that seat count increased

### Test Fully Booked Flights
1. Go to admin panel
2. Edit a flight
3. Set `seats_available` to 0
4. Save
5. Go to Flights page
6. Verify "FULLY BOOKED" overlay appears
7. Verify "Book Now" button is disabled

### Test Autocomplete
1. Go to Flights page
2. Type in destination field
3. Verify suggestions appear
4. Same for airline field

### Test Package/Deal Booking
1. Go to Packages page
2. Click "Book Package"
3. Fill in details
4. Submit
5. Check Profile for booking

## 📋 Admin Tasks

### Add New Flights
1. Go to admin panel
2. Click "Flights" → "Add Flight"
3. Fill in all details including:
   - Airline, flight number
   - Origin, destination
   - Times and date
   - Price
   - **seats_available**: 100
   - **total_seats**: 100
   - **aircraft_type**: Boeing 737
   - **baggage_allowance**: 20kg
4. Save

### Monitor Bookings
1. Admin panel → "Tickets"
2. Filter by status
3. View passenger details
4. Check seat assignments
5. Monitor refunds

### Track Revenue
1. Go to Admin Dashboard (not Django admin)
2. View total revenue card
3. See breakdown by type
4. Monitor booking trends

## 🎯 Key Features to Showcase

### For Users:
- ✈️ Visual seat selection
- 💰 Easy refund process
- 🎫 Detailed ticket with QR code
- 💺 Real-time seat availability
- 🔍 Smart search with autocomplete
- 📱 Responsive on all devices

### For Admins:
- 📊 Revenue tracking
- 👥 Passenger management
- ✈️ Flight management
- 📈 Booking statistics
- 💼 Multiple booking types

## ⚠️ Important Notes

1. **Seat Numbers**: Format is Letter+Number (e.g., A1, B3, P6)
2. **Refund Fee**: Always 20% of ticket price
3. **Seat Release**: Automatic on refund
4. **Fully Booked**: Prevents all booking attempts
5. **QR Codes**: Generated for each ticket

## 🐛 Troubleshooting

### Seats not showing?
- Check that `booked_seats` is passed to template
- Verify seat_number is saved in Ticket model

### Refund not working?
- Ensure user is logged in
- Check ticket belongs to user
- Verify ticket status is 'confirmed'

### Autocomplete not appearing?
- Check JavaScript console for errors
- Verify API endpoints are accessible
- Clear browser cache

### Fully booked not showing?
- Verify `seats_available` is 0
- Check `is_fully_booked()` method
- Refresh page

## 📞 Support

If you encounter issues:
1. Check browser console for errors
2. Check Django server logs
3. Verify migrations ran successfully
4. Ensure all files are saved
5. Restart Django server

## 🎉 You're All Set!

Your flight booking system now has:
- ✅ Professional seat selection
- ✅ Complete refund system
- ✅ Real-time availability
- ✅ Fully booked handling
- ✅ Enhanced user experience

**Enjoy your upgraded flight booking website!** 🚀
