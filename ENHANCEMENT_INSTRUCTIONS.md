# Flight Booking Enhancement - Update Instructions

## Changes Made

### 1. Multiple Passengers Feature
- Added `num_passengers` field to the Ticket model
- Updated booking form to allow selecting number of passengers (1 to available seats)
- Price calculation now shows per-passenger and total price dynamically
- Seat availability is reduced by the number of passengers booked

### 2. Phone Number Simplification
- Removed country code dropdown from phone input
- Phone number is now a simple text field
- Users can enter their phone number directly without selecting country code

### 3. Enhanced Styling & Spacing
- Improved margins and padding throughout the website
- Better spacing in forms, cards, and sections
- Enhanced visual hierarchy with proper spacing
- Rounded corners and modern card designs

### 4. Amazing Animations
- Fade-in animations for cards and sections
- Slide-in animations for navigation and headers
- Hover effects on cards, buttons, and interactive elements
- Pulse animations for important elements
- Float animations for icons
- Smooth scroll behavior
- Intersection Observer for scroll-triggered animations
- Scale and transform effects on hover
- Smooth transitions throughout

## How to Apply Changes

### Step 1: Activate Virtual Environment
```bash
cd "C:\Users\rajju\OneDrive\Pictures\Django project"
myvenv\Scripts\activate
```

### Step 2: Run Migrations
```bash
cd myProject
python manage.py migrate
```

### Step 3: Start the Server
```bash
python manage.py runserver
```

### Step 4: Test the Changes
1. Navigate to http://127.0.0.1:8000/
2. Go to Flights page
3. Select a flight and click "Book Now"
4. Notice the new "Number of Passengers" field at the top
5. Try changing the number - watch the total price update automatically
6. Notice the simplified phone number field (no country code)
7. Observe the smooth animations throughout the page
8. Scroll through the page to see scroll-triggered animations

## New Features in Booking Form

### Number of Passengers
- Located at the top of the Passenger Information section
- Minimum: 1 passenger
- Maximum: Number of available seats
- Total price updates automatically when changed
- Shows "X passenger(s)" in the price display

### Phone Number
- Simple text input field
- No country code selector
- Enter phone number directly (e.g., "9841234567")

### Price Display
- Shows "Price per Passenger"
- Shows "Total Price" with passenger count
- Updates dynamically when passenger count changes

## Animation Features

### Page Load Animations
- Cards fade in and slide up
- Navigation slides in from left/right
- Headers animate on load
- Staggered animations for form sections

### Hover Animations
- Cards lift and scale on hover
- Buttons have ripple effect
- Seats scale and rotate on hover
- Detail items slide and highlight
- Images zoom slightly

### Interactive Animations
- Form inputs lift on focus
- Selected seats pulse
- Price display animates
- Smooth transitions on all interactive elements

### Scroll Animations
- Elements fade in as you scroll
- Navbar changes on scroll
- Smooth scroll behavior throughout

## Files Modified

1. `myApp/models.py` - Added num_passengers field
2. `myApp/views.py` - Updated book_flight view
3. `myApp/templates/book_flight.html` - Updated form and JavaScript
4. `myApp/templates/base.html` - Added scroll animations
5. `myApp/static/css/style.css` - Enhanced styling and animations
6. `myApp/migrations/0007_ticket_num_passengers.py` - New migration file

## Troubleshooting

If you encounter any issues:

1. **Migration Error**: Make sure you're in the correct directory and virtual environment is activated
2. **CSS Not Loading**: Clear browser cache (Ctrl+F5)
3. **Animations Not Working**: Ensure JavaScript is enabled in your browser
4. **Price Not Updating**: Check browser console for JavaScript errors

## Notes

- The num_passengers field defaults to 1 for existing tickets
- Phone numbers are now stored without country codes
- All animations are CSS-based for better performance
- Animations are responsive and work on mobile devices
- The booking system now supports group bookings efficiently
