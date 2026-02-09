import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
django.setup()

from myApp.models import Flight, Package, Deal

print("Adding more Nepal domestic flights, packages, and deals...")

# More Nepal Domestic Flights
more_domestic = [
    {
        'airline': 'Saurya Airlines',
        'flight_number': 'SYH-201',
        'origin': 'Kathmandu',
        'destination': 'Biratnagar',
        'departure_time': '07:00',
        'arrival_time': '07:45',
        'departure_date': (datetime.now() + timedelta(days=3)).date(),
        'duration': '45m',
        'price': 110.00,
        'seats_available': 55,
        'total_seats': 100,
        'aircraft_type': 'Bombardier CRJ-200',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Buddha Air',
        'flight_number': 'U4-201',
        'origin': 'Kathmandu',
        'destination': 'Bhairahawa',
        'departure_time': '08:15',
        'arrival_time': '08:50',
        'departure_date': (datetime.now() + timedelta(days=4)).date(),
        'duration': '35m',
        'price': 105.00,
        'seats_available': 62,
        'total_seats': 100,
        'aircraft_type': 'ATR 72',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Yeti Airlines',
        'flight_number': 'YT-401',
        'origin': 'Kathmandu',
        'destination': 'Nepalgunj',
        'departure_time': '09:30',
        'arrival_time': '10:30',
        'departure_date': (datetime.now() + timedelta(days=5)).date(),
        'duration': '1h',
        'price': 130.00,
        'seats_available': 48,
        'total_seats': 100,
        'aircraft_type': 'ATR 72',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Shree Airlines',
        'flight_number': 'SHA-301',
        'origin': 'Pokhara',
        'destination': 'Kathmandu',
        'departure_time': '14:00',
        'arrival_time': '14:30',
        'departure_date': (datetime.now() + timedelta(days=6)).date(),
        'duration': '30m',
        'price': 120.00,
        'seats_available': 58,
        'total_seats': 100,
        'aircraft_type': 'Jetstream 41',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Buddha Air',
        'flight_number': 'U4-701',
        'origin': 'Kathmandu',
        'destination': 'Simara',
        'departure_time': '10:45',
        'arrival_time': '11:10',
        'departure_date': (datetime.now() + timedelta(days=7)).date(),
        'duration': '25m',
        'price': 90.00,
        'seats_available': 70,
        'total_seats': 100,
        'aircraft_type': 'Beechcraft 1900D',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Yeti Airlines',
        'flight_number': 'YT-501',
        'origin': 'Kathmandu',
        'destination': 'Tumlingtar',
        'departure_time': '06:45',
        'arrival_time': '07:30',
        'departure_date': (datetime.now() + timedelta(days=8)).date(),
        'duration': '45m',
        'price': 140.00,
        'seats_available': 35,
        'total_seats': 100,
        'aircraft_type': 'Twin Otter',
        'baggage_allowance': '10kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Summit Air',
        'flight_number': 'SMT-101',
        'origin': 'Kathmandu',
        'destination': 'Phaplu',
        'departure_time': '07:30',
        'arrival_time': '08:00',
        'departure_date': (datetime.now() + timedelta(days=9)).date(),
        'duration': '30m',
        'price': 160.00,
        'seats_available': 18,
        'total_seats': 100,
        'aircraft_type': 'Dornier 228',
        'baggage_allowance': '10kg',
        'flight_type': 'domestic'
    },
    {
        'airline': 'Tara Air',
        'flight_number': 'TA-183',
        'origin': 'Kathmandu',
        'destination': 'Janakpur',
        'departure_time': '11:00',
        'arrival_time': '11:40',
        'departure_date': (datetime.now() + timedelta(days=10)).date(),
        'duration': '40m',
        'price': 115.00,
        'seats_available': 42,
        'total_seats': 100,
        'aircraft_type': 'Twin Otter',
        'baggage_allowance': '15kg',
        'flight_type': 'domestic'
    },
]

for flight_data in more_domestic:
    flight, created = Flight.objects.get_or_create(
        flight_number=flight_data['flight_number'],
        defaults=flight_data
    )
    if created:
        print(f"✓ Added flight: {flight.airline} {flight.flight_number}")

# More Nepal Packages
more_packages = [
    {
        'name': 'Langtang Valley Trek',
        'description': 'Trek through the beautiful Langtang Valley, known as the "Valley of Glaciers". Experience Tamang culture, visit cheese factories, and enjoy stunning mountain views. Perfect for those seeking a less crowded trekking experience.',
        'destination': 'Nepal - Langtang Region',
        'price': 899.00,
        'duration': '8 Days / 7 Nights',
        'includes': 'Guide, Permits, Tea Houses, Meals, Transportation from Kathmandu'
    },
    {
        'name': 'Manaslu Circuit Trek',
        'description': 'Circle the eighth highest mountain in the world. Experience remote villages, diverse landscapes, and cross the challenging Larkya La Pass. A true adventure for experienced trekkers.',
        'destination': 'Nepal - Manaslu Region',
        'price': 1599.00,
        'duration': '16 Days / 15 Nights',
        'includes': 'Guide, Porter, Permits, Tea Houses, All Meals, Transportation'
    },
    {
        'name': 'Rara Lake Adventure',
        'description': 'Visit Nepal\'s largest lake in the remote far-western region. Pristine nature, unique wildlife, and peaceful surroundings. Includes flight to Talcha Airport and trekking around the lake.',
        'destination': 'Nepal - Rara Lake',
        'price': 1199.00,
        'duration': '10 Days / 9 Nights',
        'includes': 'Domestic Flights, Guide, Camping Equipment, Meals, Permits'
    },
    {
        'name': 'Nagarkot Sunrise & Bhaktapur Tour',
        'description': 'Short getaway to witness stunning Himalayan sunrise from Nagarkot. Explore the ancient city of Bhaktapur with its temples, palaces, and traditional pottery squares.',
        'destination': 'Nepal - Kathmandu Valley',
        'price': 299.00,
        'duration': '2 Days / 1 Night',
        'includes': 'Hotel, Transportation, Guide, Entrance Fees, Breakfast'
    },
    {
        'name': 'Ghorepani Poon Hill Trek',
        'description': 'Short and scenic trek perfect for beginners. Witness spectacular sunrise over Annapurna and Dhaulagiri ranges from Poon Hill. Walk through rhododendron forests and traditional Gurung villages.',
        'destination': 'Nepal - Annapurna Region',
        'price': 499.00,
        'duration': '5 Days / 4 Nights',
        'includes': 'Guide, Tea Houses, Meals, Permits, Transportation'
    },
]

for pkg_data in more_packages:
    package, created = Package.objects.get_or_create(
        name=pkg_data['name'],
        defaults=pkg_data
    )
    if created:
        print(f"✓ Added package: {package.name}")

# More Nepal Deals
more_deals = [
    {
        'title': 'Bandipur Village Homestay',
        'description': 'Experience authentic Newari culture in the hilltop village of Bandipur. Stay with local families, enjoy traditional food, and explore preserved architecture. Peaceful mountain views included.',
        'destination': 'Nepal - Bandipur',
        'original_price': 349.00,
        'discounted_price': 249.00,
        'discount_percentage': 29,
        'valid_until': (datetime.now() + timedelta(days=35)).date(),
        'is_active': True
    },
    {
        'title': 'Paragliding in Pokhara',
        'description': 'Fly like a bird over Pokhara valley! Tandem paragliding with experienced pilots. Includes hotel pickup, flight, photos/videos, and certificate. Unforgettable aerial views of Phewa Lake and Annapurna.',
        'destination': 'Nepal - Pokhara',
        'original_price': 199.00,
        'discounted_price': 149.00,
        'discount_percentage': 25,
        'valid_until': (datetime.now() + timedelta(days=40)).date(),
        'is_active': True
    },
    {
        'title': 'Everest Mountain Flight',
        'description': 'One-hour scenic flight to view Mount Everest and other Himalayan peaks up close. Perfect for those who want to see Everest without trekking. Includes breakfast and window seat guarantee.',
        'destination': 'Nepal - Everest',
        'original_price': 299.00,
        'discounted_price': 229.00,
        'discount_percentage': 23,
        'valid_until': (datetime.now() + timedelta(days=30)).date(),
        'is_active': True
    },
    {
        'title': 'Rafting on Trishuli River',
        'description': 'Thrilling white water rafting adventure on Trishuli River. Suitable for beginners and families. Includes safety equipment, guide, lunch, and transportation from Kathmandu.',
        'destination': 'Nepal - Trishuli',
        'original_price': 149.00,
        'discounted_price': 99.00,
        'discount_percentage': 34,
        'valid_until': (datetime.now() + timedelta(days=45)).date(),
        'is_active': True
    },
]

for deal_data in more_deals:
    deal, created = Deal.objects.get_or_create(
        title=deal_data['title'],
        defaults=deal_data
    )
    if created:
        print(f"✓ Added deal: {deal.title}")

print("\n✅ More Nepal destinations added successfully!")
print(f"Total Flights: {Flight.objects.count()}")
print(f"Domestic Flights: {Flight.objects.filter(flight_type='domestic').count()}")
print(f"Total Packages: {Package.objects.count()}")
print(f"Total Deals: {Deal.objects.count()}")
