#!/bin/bash

echo "Running Django migrations..."
cd "/mnt/c/Users/rajju/OneDrive/Pictures/Django project/myProject"

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

echo "Migrations completed!"
echo ""
echo "Summary of changes:"
echo "✓ Added seat selection with visual seat map"
echo "✓ Added refund functionality (20% cancellation fee)"
echo "✓ Added passenger details (passport, DOB, nationality)"
echo "✓ Added seat class selection (Economy/Business/First)"
echo "✓ Added special requests field"
echo "✓ Added fully booked flight detection"
echo "✓ Added low seat warnings"
echo "✓ Added ticket detail view with QR code"
echo "✓ Added PackageBooking and DealBooking models"
echo "✓ Added autocomplete for destinations and airlines"
echo "✓ Added total revenue in admin dashboard"
echo "✓ Added aircraft type and baggage allowance"
echo ""
echo "Next steps:"
echo "1. Run: python manage.py runserver"
echo "2. Access admin panel to add/update flight data"
echo "3. Test the booking flow with seat selection"
echo "4. Test refund functionality"
