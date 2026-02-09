import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
django.setup()

from myApp.models import Flight, Package, Deal

# Clear existing data (optional)
print("Adding sample data...")

# Add Flights
flights_data = [
    {
        'airline': 'Emirates',
        'flight_number': 'EK215',
        'origin': 'New York',
        'destination': 'Dubai',
        'departure_time': '23:45',
        'arrival_time': '19:30',
        'departure_date': (datetime.now() + timedelta(days=5)).date(),
        'duration': '12h 45m',
        'price': 899.00,
        'seats_available': 45,
        'total_seats': 100,
        'aircraft_type': 'Airbus A380',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Singapore Airlines',
        'flight_number': 'SQ25',
        'origin': 'Los Angeles',
        'destination': 'Singapore',
        'departure_time': '00:05',
        'arrival_time': '07:30',
        'departure_date': (datetime.now() + timedelta(days=7)).date(),
        'duration': '17h 25m',
        'price': 1250.00,
        'seats_available': 32,
        'total_seats': 100,
        'aircraft_type': 'Boeing 777-300ER',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'British Airways',
        'flight_number': 'BA117',
        'origin': 'London',
        'destination': 'New York',
        'departure_time': '11:30',
        'arrival_time': '14:15',
        'departure_date': (datetime.now() + timedelta(days=3)).date(),
        'duration': '7h 45m',
        'price': 650.00,
        'seats_available': 58,
        'total_seats': 100,
        'aircraft_type': 'Boeing 787-9',
        'baggage_allowance': '23kg'
    },
    {
        'airline': 'Qatar Airways',
        'flight_number': 'QR921',
        'origin': 'Paris',
        'destination': 'Doha',
        'departure_time': '15:20',
        'arrival_time': '23:45',
        'departure_date': (datetime.now() + timedelta(days=10)).date(),
        'duration': '6h 25m',
        'price': 720.00,
        'seats_available': 41,
        'total_seats': 100,
        'aircraft_type': 'Airbus A350-900',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Lufthansa',
        'flight_number': 'LH456',
        'origin': 'Frankfurt',
        'destination': 'Tokyo',
        'departure_time': '13:45',
        'arrival_time': '08:30',
        'departure_date': (datetime.now() + timedelta(days=12)).date(),
        'duration': '11h 45m',
        'price': 980.00,
        'seats_available': 27,
        'total_seats': 100,
        'aircraft_type': 'Boeing 747-8',
        'baggage_allowance': '23kg'
    },
    {
        'airline': 'Air France',
        'flight_number': 'AF83',
        'origin': 'Paris',
        'destination': 'San Francisco',
        'departure_time': '10:15',
        'arrival_time': '12:45',
        'departure_date': (datetime.now() + timedelta(days=6)).date(),
        'duration': '11h 30m',
        'price': 850.00,
        'seats_available': 52,
        'total_seats': 100,
        'aircraft_type': 'Boeing 777-200ER',
        'baggage_allowance': '23kg'
    },
    {
        'airline': 'Cathay Pacific',
        'flight_number': 'CX880',
        'origin': 'Hong Kong',
        'destination': 'Los Angeles',
        'departure_time': '16:00',
        'arrival_time': '13:30',
        'departure_date': (datetime.now() + timedelta(days=8)).date(),
        'duration': '12h 30m',
        'price': 920.00,
        'seats_available': 38,
        'total_seats': 100,
        'aircraft_type': 'Airbus A350-1000',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Delta Airlines',
        'flight_number': 'DL159',
        'origin': 'Atlanta',
        'destination': 'Amsterdam',
        'departure_time': '18:40',
        'arrival_time': '09:15',
        'departure_date': (datetime.now() + timedelta(days=4)).date(),
        'duration': '8h 35m',
        'price': 680.00,
        'seats_available': 64,
        'total_seats': 100,
        'aircraft_type': 'Airbus A330-300',
        'baggage_allowance': '23kg'
    },
    {
        'airline': 'Turkish Airlines',
        'flight_number': 'TK1',
        'origin': 'Istanbul',
        'destination': 'New York',
        'departure_time': '01:15',
        'arrival_time': '05:30',
        'departure_date': (datetime.now() + timedelta(days=9)).date(),
        'duration': '11h 15m',
        'price': 750.00,
        'seats_available': 47,
        'total_seats': 100,
        'aircraft_type': 'Boeing 777-300ER',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'ANA',
        'flight_number': 'NH9',
        'origin': 'Tokyo',
        'destination': 'Chicago',
        'departure_time': '17:55',
        'arrival_time': '15:10',
        'departure_date': (datetime.now() + timedelta(days=11)).date(),
        'duration': '11h 15m',
        'price': 1100.00,
        'seats_available': 29,
        'total_seats': 100,
        'aircraft_type': 'Boeing 787-9',
        'baggage_allowance': '23kg'
    }
]

for flight_data in flights_data:
    flight, created = Flight.objects.get_or_create(
        flight_number=flight_data['flight_number'],
        defaults=flight_data
    )
    if created:
        print(f"✓ Added flight: {flight.airline} {flight.flight_number}")

# Add Packages
packages_data = [
    {
        'name': 'Tropical Paradise - Maldives',
        'description': 'Experience luxury in the Maldives with overwater bungalows, pristine beaches, and world-class diving. Includes round-trip flights, 7 nights accommodation, daily breakfast, and water sports activities.',
        'destination': 'Maldives',
        'price': 2499.00,
        'duration': '7 Days / 6 Nights',
        'includes': 'Flights, 5-Star Resort, Meals, Water Sports, Spa Treatment'
    },
    {
        'name': 'European Grand Tour',
        'description': 'Visit 5 iconic European cities: Paris, Rome, Barcelona, Amsterdam, and London. Guided tours, museum passes, and authentic local experiences included.',
        'destination': 'Europe',
        'price': 3299.00,
        'duration': '14 Days / 13 Nights',
        'includes': 'Flights, Hotels, City Tours, Museum Passes, Some Meals'
    },
    {
        'name': 'Dubai Luxury Experience',
        'description': 'Discover the wonders of Dubai with stays at 5-star hotels, desert safari, Burj Khalifa tickets, and shopping tours. Perfect blend of modern luxury and traditional culture.',
        'destination': 'Dubai',
        'price': 1899.00,
        'duration': '5 Days / 4 Nights',
        'includes': 'Flights, 5-Star Hotel, Desert Safari, Burj Khalifa, City Tour'
    },
    {
        'name': 'Tokyo & Kyoto Adventure',
        'description': 'Immerse yourself in Japanese culture with visits to ancient temples, modern Tokyo, traditional tea ceremonies, and authentic cuisine experiences.',
        'destination': 'Japan',
        'price': 2799.00,
        'duration': '10 Days / 9 Nights',
        'includes': 'Flights, Hotels, JR Pass, Guided Tours, Cultural Experiences'
    },
    {
        'name': 'Caribbean Island Hopping',
        'description': 'Explore multiple Caribbean islands including Jamaica, Bahamas, and Barbados. Beach resorts, water activities, and island tours included.',
        'destination': 'Caribbean',
        'price': 2199.00,
        'duration': '8 Days / 7 Nights',
        'includes': 'Flights, Beach Resorts, Island Tours, Water Activities, Meals'
    },
    {
        'name': 'Australian Outback & Reef',
        'description': 'Experience the best of Australia with Sydney Opera House, Great Barrier Reef snorkeling, and Outback adventures. Unforgettable wildlife encounters.',
        'destination': 'Australia',
        'price': 3599.00,
        'duration': '12 Days / 11 Nights',
        'includes': 'Flights, Hotels, Reef Tour, Wildlife Park, City Tours'
    }
]

for pkg_data in packages_data:
    package, created = Package.objects.get_or_create(
        name=pkg_data['name'],
        defaults=pkg_data
    )
    if created:
        print(f"✓ Added package: {package.name}")

# Add Deals
deals_data = [
    {
        'title': 'Flash Sale: Bali Paradise',
        'description': 'Limited time offer! Fly to Bali and stay at a luxury beach resort. Includes spa treatments, daily breakfast, and airport transfers. Book now before it\'s gone!',
        'destination': 'Bali',
        'original_price': 1599.00,
        'discounted_price': 999.00,
        'discount_percentage': 38,
        'valid_until': (datetime.now() + timedelta(days=15)).date(),
        'is_active': True
    },
    {
        'title': 'Early Bird: Iceland Northern Lights',
        'description': 'Witness the magical Northern Lights in Iceland. Package includes flights, hotel, Blue Lagoon entry, and Northern Lights tour. Early bird special!',
        'destination': 'Iceland',
        'original_price': 2299.00,
        'discounted_price': 1599.00,
        'discount_percentage': 30,
        'valid_until': (datetime.now() + timedelta(days=20)).date(),
        'is_active': True
    },
    {
        'title': 'Weekend Getaway: New York City',
        'description': 'Quick escape to NYC! Includes round-trip flights, 3-star hotel in Manhattan, and hop-on-hop-off bus tour. Perfect for a weekend adventure.',
        'destination': 'New York',
        'original_price': 899.00,
        'discounted_price': 599.00,
        'discount_percentage': 33,
        'valid_until': (datetime.now() + timedelta(days=10)).date(),
        'is_active': True
    },
    {
        'title': 'Summer Special: Greek Islands',
        'description': 'Island hop through Santorini, Mykonos, and Crete. Includes flights, ferry passes, hotels, and sunset cruise. Summer special pricing!',
        'destination': 'Greece',
        'original_price': 2499.00,
        'discounted_price': 1799.00,
        'discount_percentage': 28,
        'valid_until': (datetime.now() + timedelta(days=25)).date(),
        'is_active': True
    },
    {
        'title': 'Last Minute: Thailand Beach Escape',
        'description': 'Last minute deal to Phuket! Beachfront resort, Thai cooking class, island tours, and more. Limited availability!',
        'destination': 'Thailand',
        'original_price': 1799.00,
        'discounted_price': 1199.00,
        'discount_percentage': 33,
        'valid_until': (datetime.now() + timedelta(days=7)).date(),
        'is_active': True
    }
]

for deal_data in deals_data:
    deal, created = Deal.objects.get_or_create(
        title=deal_data['title'],
        defaults=deal_data
    )
    if created:
        print(f"✓ Added deal: {deal.title}")

print("\n✅ Sample data added successfully!")
print(f"Total Flights: {Flight.objects.count()}")
print(f"Total Packages: {Package.objects.count()}")
print(f"Total Deals: {Deal.objects.count()}")
