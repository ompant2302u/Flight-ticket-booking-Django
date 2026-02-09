# Flight Ticket Management System - Setup Instructions

## Installation Complete! 🎉

Your Django flight ticket management system has been successfully enhanced with all the requested features.

## What's Been Added:

### Backend Features:
- ✅ Enhanced Flight model with date, time, airline, seats, duration
- ✅ Package model for travel packages
- ✅ Deal model for special offers
- ✅ Enhanced Ticket/Booking model with status and payment tracking
- ✅ Extended Profile model with more fields
- ✅ Search and filter functionality
- ✅ Admin dashboard with analytics
- ✅ User authentication (login, signup, logout)
- ✅ Profile management with photo upload

### Frontend Features:
- ✅ Modern responsive navbar with sticky scroll effect
- ✅ Mobile-responsive design with sliding menu
- ✅ Hero section with search form
- ✅ Animated cards for flights, packages, and deals
- ✅ Profile dropdown menu
- ✅ Beautiful forms with validation
- ✅ Ticket confirmation with QR code
- ✅ Admin dashboard with stats
- ✅ Smooth animations and transitions
- ✅ Modern color scheme with Inter and Outfit fonts

## Setup Steps:

### 1. Navigate to project directory:
```bash
cd "/mnt/c/Users/rajju/OneDrive/Pictures/Django project/myProject"
```

### 2. Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

### 4. Create media directories:
```bash
mkdir -p media/profiles media/packages media/deals
```

### 5. Run the development server:
```bash
python manage.py runserver
```

### 6. Access the application:
- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Admin Dashboard: http://127.0.0.1:8000/admin-dashboard/ (requires staff user)

## Adding Sample Data:

### Option 1: Through Django Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Add Flights, Packages, and Deals

### Option 2: Using Django Shell
```bash
python manage.py shell
```

Then run:
```python
from myApp.models import Flight, Package, Deal
from datetime import date, time

# Add sample flights
Flight.objects.create(
    flight_number="SK101",
    origin="New York",
    destination="London",
    country="UK",
    departure_date=date(2026, 3, 15),
    departure_time=time(10, 30),
    arrival_time=time(22, 45),
    price=599.99,
    airline="SkyVoyage Airlines",
    seats_available=150,
    duration="7h 15m"
)

Flight.objects.create(
    flight_number="SK202",
    origin="Los Angeles",
    destination="Tokyo",
    country="Japan",
    departure_date=date(2026, 3, 20),
    departure_time=time(14, 0),
    arrival_time=time(18, 30),
    price=899.99,
    airline="Pacific Air",
    seats_available=200,
    duration="11h 30m"
)

# Add sample package
Package.objects.create(
    name="Paris Getaway",
    description="Experience the city of lights with our exclusive 5-day package",
    destination="Paris, France",
    price=1299.99,
    duration="5 Days / 4 Nights",
    includes="Flight, Hotel, Breakfast, City Tour"
)

# Add sample deal
Deal.objects.create(
    title="Summer Special - Bali",
    description="Limited time offer for tropical paradise",
    destination="Bali, Indonesia",
    original_price=1500.00,
    discounted_price=999.00,
    discount_percentage=33,
    valid_until=date(2026, 6, 30),
    is_active=True
)
```

## Features Overview:

### For Users:
- Browse and search flights with filters
- View travel packages and special deals
- Book flights with instant confirmation
- Create and manage profile with photo
- View booking history
- Download/print tickets with QR codes

### For Admins:
- Full CRUD operations via Django admin
- Custom admin dashboard with analytics
- View recent bookings
- Track popular destinations
- Manage flights, packages, deals, and users

## File Structure:
```
myProject/
├── myApp/
│   ├── models.py          # Enhanced models
│   ├── views.py           # All views with search/filters
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── signals.py         # Profile auto-creation
│   ├── templates/         # All HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── flights.html
│   │   ├── packages.html
│   │   ├── deals.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── profile.html
│   │   ├── edit_profile.html
│   │   ├── book_flight.html
│   │   ├── ticket_overview.html
│   │   └── admin_dashboard.html
│   └── static/
│       ├── css/
│       │   └── style.css  # Complete styling with animations
│       └── js/
│           └── script.js  # Interactive features
├── myProject/
│   ├── settings.py        # Updated configuration
│   └── urls.py            # Main URL config
└── media/                 # User uploads
```

## Customization Tips:

### Change Colors:
Edit `static/css/style.css` and modify the `:root` variables:
```css
:root {
    --primary: #ff6b6b;      /* Main accent color */
    --secondary: #4ecdc4;    /* Secondary color */
    --dark: #2d3436;         /* Text color */
}
```

### Add More Animations:
Check `static/js/script.js` for animation functions

### Modify Templates:
All templates extend `base.html` for easy customization

## Troubleshooting:

### Static files not loading:
```bash
python manage.py collectstatic
```

### Database errors:
```bash
python manage.py migrate --run-syncdb
```

### Profile not created automatically:
The signals.py file handles this. Make sure myApp is in INSTALLED_APPS.

## Security Notes:
- Change SECRET_KEY in production
- Set DEBUG = False in production
- Configure ALLOWED_HOSTS
- Use environment variables for sensitive data
- Enable HTTPS in production

## Next Steps:
1. Add email notifications for bookings
2. Integrate payment gateway (Stripe/PayPal)
3. Add booking cancellation feature
4. Implement seat selection
5. Add flight reviews and ratings
6. Create booking reports for admin

Enjoy your new flight ticket management system! ✈️
