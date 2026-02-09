"""
Sample data script for Flight Ticket Management System
Run this with: python manage.py shell < add_sample_data.py
"""

from myApp.models import Flight, Package, Deal
from datetime import date, time, timedelta

print("Adding sample data...")

# Clear existing data (optional)
# Flight.objects.all().delete()
# Package.objects.all().delete()
# Deal.objects.all().delete()

# Add Flights
flights_data = [
    {
        'flight_number': 'SK101',
        'origin': 'New York',
        'destination': 'London',
        'country': 'UK',
        'departure_date': date.today() + timedelta(days=15),
        'departure_time': time(10, 30),
        'arrival_time': time(22, 45),
        'price': 599.99,
        'airline': 'SkyVoyage Airlines',
        'seats_available': 150,
        'duration': '7h 15m'
    },
    {
        'flight_number': 'SK202',
        'origin': 'Los Angeles',
        'destination': 'Tokyo',
        'country': 'Japan',
        'departure_date': date.today() + timedelta(days=20),
        'departure_time': time(14, 0),
        'arrival_time': time(18, 30),
        'price': 899.99,
        'airline': 'Pacific Air',
        'seats_available': 200,
        'duration': '11h 30m'
    },
    {
        'flight_number': 'SK303',
        'origin': 'Chicago',
        'destination': 'Paris',
        'country': 'France',
        'departure_date': date.today() + timedelta(days=25),
        'departure_time': time(16, 45),
        'arrival_time': time(8, 30),
        'price': 749.99,
        'airline': 'Euro Wings',
        'seats_available': 180,
        'duration': '8h 45m'
    },
    {
        'flight_number': 'SK404',
        'origin': 'Miami',
        'destination': 'Dubai',
        'country': 'UAE',
        'departure_date': date.today() + timedelta(days=30),
        'departure_time': time(22, 0),
        'arrival_time': time(19, 15),
        'price': 1099.99,
        'airline': 'Emirates Sky',
        'seats_available': 220,
        'duration': '14h 15m'
    },
    {
        'flight_number': 'SK505',
        'origin': 'San Francisco',
        'destination': 'Sydney',
        'country': 'Australia',
        'departure_date': date.today() + timedelta(days=35),
        'departure_time': time(11, 0),
        'arrival_time': time(20, 30),
        'price': 1299.99,
        'airline': 'Oceanic Air',
        'seats_available': 190,
        'duration': '15h 30m'
    },
    {
        'flight_number': 'SK606',
        'origin': 'Boston',
        'destination': 'Rome',
        'country': 'Italy',
        'departure_date': date.today() + timedelta(days=18),
        'departure_time': time(19, 30),
        'arrival_time': time(9, 45),
        'price': 679.99,
        'airline': 'Mediterranean Air',
        'seats_available': 160,
        'duration': '9h 15m'
    }
]

for flight_data in flights_data:
    flight, created = Flight.objects.get_or_create(
        flight_number=flight_data['flight_number'],
        defaults=flight_data
    )
    if created:
        print(f"✓ Created flight: {flight.flight_number}")

# Add Packages
packages_data = [
    {
        'name': 'Paris Romantic Getaway',
        'description': 'Experience the city of lights with our exclusive 5-day package. Visit the Eiffel Tower, Louvre Museum, and enjoy Seine river cruise.',
        'destination': 'Paris, France',
        'price': 1299.99,
        'duration': '5 Days / 4 Nights',
        'includes': 'Round-trip flights, 4-star hotel, Daily breakfast, City tour, Museum passes'
    },
    {
        'name': 'Tokyo Adventure',
        'description': 'Discover the perfect blend of tradition and modernity in Japan\'s capital city.',
        'destination': 'Tokyo, Japan',
        'price': 1899.99,
        'duration': '7 Days / 6 Nights',
        'includes': 'Flights, Luxury hotel, Breakfast & dinner, Guided tours, JR Pass'
    },
    {
        'name': 'Dubai Luxury Experience',
        'description': 'Indulge in the ultimate luxury with desert safaris, shopping, and world-class dining.',
        'destination': 'Dubai, UAE',
        'price': 2199.99,
        'duration': '6 Days / 5 Nights',
        'includes': 'Business class flights, 5-star hotel, All meals, Desert safari, Burj Khalifa tickets'
    },
    {
        'name': 'Bali Beach Paradise',
        'description': 'Relax on pristine beaches and explore ancient temples in this tropical paradise.',
        'destination': 'Bali, Indonesia',
        'price': 999.99,
        'duration': '5 Days / 4 Nights',
        'includes': 'Flights, Beach resort, Breakfast, Spa treatment, Temple tours'
    },
    {
        'name': 'New York City Explorer',
        'description': 'See the best of NYC with Broadway shows, museums, and iconic landmarks.',
        'destination': 'New York, USA',
        'price': 1499.99,
        'duration': '4 Days / 3 Nights',
        'includes': 'Flights, Manhattan hotel, Broadway tickets, City pass, Food tour'
    }
]

for package_data in packages_data:
    package, created = Package.objects.get_or_create(
        name=package_data['name'],
        defaults=package_data
    )
    if created:
        print(f"✓ Created package: {package.name}")

# Add Deals
deals_data = [
    {
        'title': 'Summer Special - Bali',
        'description': 'Limited time offer for tropical paradise. Book now and save big on your dream vacation!',
        'destination': 'Bali, Indonesia',
        'original_price': 1500.00,
        'discounted_price': 999.00,
        'discount_percentage': 33,
        'valid_until': date.today() + timedelta(days=60),
        'is_active': True
    },
    {
        'title': 'Early Bird - London',
        'description': 'Book 3 months in advance and get amazing discounts on flights to London.',
        'destination': 'London, UK',
        'original_price': 799.00,
        'discounted_price': 549.00,
        'discount_percentage': 31,
        'valid_until': date.today() + timedelta(days=45),
        'is_active': True
    },
    {
        'title': 'Weekend Getaway - Paris',
        'description': 'Perfect weekend escape to the city of love with exclusive hotel deals.',
        'destination': 'Paris, France',
        'original_price': 1200.00,
        'discounted_price': 899.00,
        'discount_percentage': 25,
        'valid_until': date.today() + timedelta(days=30),
        'is_active': True
    },
    {
        'title': 'Flash Sale - Dubai',
        'description': 'Hurry! Limited seats available for this incredible Dubai deal.',
        'destination': 'Dubai, UAE',
        'original_price': 1800.00,
        'discounted_price': 1299.00,
        'discount_percentage': 28,
        'valid_until': date.today() + timedelta(days=15),
        'is_active': True
    },
    {
        'title': 'Group Discount - Sydney',
        'description': 'Travel with friends and family. Special group rates for Sydney packages.',
        'destination': 'Sydney, Australia',
        'original_price': 2000.00,
        'discounted_price': 1499.00,
        'discount_percentage': 25,
        'valid_until': date.today() + timedelta(days=90),
        'is_active': True
    }
]

for deal_data in deals_data:
    deal, created = Deal.objects.get_or_create(
        title=deal_data['title'],
        defaults=deal_data
    )
    if created:
        print(f"✓ Created deal: {deal.title}")

print("\n✅ Sample data added successfully!")
print(f"Total Flights: {Flight.objects.count()}")
print(f"Total Packages: {Package.objects.count()}")
print(f"Total Deals: {Deal.objects.count()}")
