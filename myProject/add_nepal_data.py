import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
django.setup()

from myApp.models import Flight, Package, Deal

print("Adding Nepal and world destinations...")

# Nepal Domestic Flights
nepal_domestic = [
    {
        'airline': 'Buddha Air',
        'flight_number': 'U4-101',
        'origin': 'Kathmandu',
        'destination': 'Pokhara',
        'departure_time': '06:30',
        'arrival_time': '07:00',
        'departure_date': (datetime.now() + timedelta(days=2)).date(),
        'duration': '30m',
        'price': 120.00,
        'seats_available': 68,
        'total_seats': 100,
        'aircraft_type': 'ATR 72',
        'baggage_allowance': '15kg'
    },
    {
        'airline': 'Yeti Airlines',
        'flight_number': 'YT-691',
        'origin': 'Kathmandu',
        'destination': 'Lukla',
        'departure_time': '07:15',
        'arrival_time': '07:55',
        'departure_date': (datetime.now() + timedelta(days=3)).date(),
        'duration': '40m',
        'price': 180.00,
        'seats_available': 12,
        'total_seats': 100,
        'aircraft_type': 'Twin Otter',
        'baggage_allowance': '10kg'
    },
    {
        'airline': 'Shree Airlines',
        'flight_number': 'SHA-211',
        'origin': 'Kathmandu',
        'destination': 'Bharatpur',
        'departure_time': '09:00',
        'arrival_time': '09:25',
        'departure_date': (datetime.now() + timedelta(days=4)).date(),
        'duration': '25m',
        'price': 95.00,
        'seats_available': 45,
        'total_seats': 100,
        'aircraft_type': 'Jetstream 41',
        'baggage_allowance': '15kg'
    },
    {
        'airline': 'Buddha Air',
        'flight_number': 'U4-505',
        'origin': 'Pokhara',
        'destination': 'Jomsom',
        'departure_time': '08:30',
        'arrival_time': '09:00',
        'departure_date': (datetime.now() + timedelta(days=5)).date(),
        'duration': '30m',
        'price': 150.00,
        'seats_available': 28,
        'total_seats': 100,
        'aircraft_type': 'Twin Otter',
        'baggage_allowance': '10kg'
    },
]

# Nepal International Flights
nepal_international = [
    {
        'airline': 'Nepal Airlines',
        'flight_number': 'RA-225',
        'origin': 'Kathmandu',
        'destination': 'Delhi',
        'departure_time': '14:30',
        'arrival_time': '15:45',
        'departure_date': (datetime.now() + timedelta(days=6)).date(),
        'duration': '1h 15m',
        'price': 250.00,
        'seats_available': 52,
        'total_seats': 100,
        'aircraft_type': 'Airbus A320',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Himalaya Airlines',
        'flight_number': 'H9-771',
        'origin': 'Kathmandu',
        'destination': 'Doha',
        'departure_time': '22:45',
        'arrival_time': '02:30',
        'departure_date': (datetime.now() + timedelta(days=7)).date(),
        'duration': '4h 45m',
        'price': 450.00,
        'seats_available': 38,
        'total_seats': 100,
        'aircraft_type': 'Airbus A320',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Nepal Airlines',
        'flight_number': 'RA-316',
        'origin': 'Kathmandu',
        'destination': 'Bangkok',
        'departure_time': '10:15',
        'arrival_time': '14:30',
        'departure_date': (datetime.now() + timedelta(days=8)).date(),
        'duration': '3h 15m',
        'price': 320.00,
        'seats_available': 44,
        'total_seats': 100,
        'aircraft_type': 'Airbus A330',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Air India',
        'flight_number': 'AI-215',
        'origin': 'Delhi',
        'destination': 'Kathmandu',
        'departure_time': '08:00',
        'arrival_time': '09:30',
        'departure_date': (datetime.now() + timedelta(days=9)).date(),
        'duration': '1h 30m',
        'price': 280.00,
        'seats_available': 56,
        'total_seats': 100,
        'aircraft_type': 'Boeing 737',
        'baggage_allowance': '23kg'
    },
]

# Additional Popular International Flights
popular_international = [
    {
        'airline': 'Etihad Airways',
        'flight_number': 'EY-103',
        'origin': 'Abu Dhabi',
        'destination': 'London',
        'departure_time': '02:25',
        'arrival_time': '07:10',
        'departure_date': (datetime.now() + timedelta(days=10)).date(),
        'duration': '7h 45m',
        'price': 780.00,
        'seats_available': 42,
        'total_seats': 100,
        'aircraft_type': 'Boeing 787-9',
        'baggage_allowance': '30kg'
    },
    {
        'airline': 'Korean Air',
        'flight_number': 'KE-601',
        'origin': 'Seoul',
        'destination': 'Los Angeles',
        'departure_time': '19:50',
        'arrival_time': '15:20',
        'departure_date': (datetime.now() + timedelta(days=11)).date(),
        'duration': '11h 30m',
        'price': 1050.00,
        'seats_available': 35,
        'total_seats': 100,
        'aircraft_type': 'Boeing 777-300ER',
        'baggage_allowance': '23kg'
    },
]

all_flights = nepal_domestic + nepal_international + popular_international

for flight_data in all_flights:
    flight, created = Flight.objects.get_or_create(
        flight_number=flight_data['flight_number'],
        defaults=flight_data
    )
    if created:
        print(f"✓ Added flight: {flight.airline} {flight.flight_number}")

# Nepal Packages
nepal_packages = [
    {
        'name': 'Everest Base Camp Trek',
        'description': 'Experience the ultimate Himalayan adventure with a trek to Everest Base Camp. Includes flights to Lukla, experienced guides, tea house accommodation, and all permits. Witness breathtaking mountain views and Sherpa culture.',
        'destination': 'Nepal - Everest Region',
        'price': 1499.00,
        'duration': '14 Days / 13 Nights',
        'includes': 'Flights, Trekking Permits, Guide, Accommodation, Meals, Airport Transfers'
    },
    {
        'name': 'Annapurna Circuit Adventure',
        'description': 'Trek through diverse landscapes from subtropical forests to high mountain passes. Experience traditional villages, hot springs, and stunning Annapurna views. Perfect for adventure seekers.',
        'destination': 'Nepal - Annapurna Region',
        'price': 1299.00,
        'duration': '12 Days / 11 Nights',
        'includes': 'Domestic Flights, Permits, Guide, Tea Houses, Meals, Transportation'
    },
    {
        'name': 'Kathmandu Valley Cultural Tour',
        'description': 'Explore UNESCO World Heritage Sites including Pashupatinath, Boudhanath, Swayambhunath, and Durbar Squares. Experience rich Nepali culture, ancient temples, and traditional cuisine.',
        'destination': 'Nepal - Kathmandu Valley',
        'price': 599.00,
        'duration': '5 Days / 4 Nights',
        'includes': 'Hotel, Guided Tours, Entrance Fees, Cultural Shows, Meals'
    },
    {
        'name': 'Pokhara Lakeside Retreat',
        'description': 'Relax by the serene Phewa Lake with views of Annapurna and Machhapuchhre. Includes paragliding, boating, sunrise at Sarangkot, and visits to caves and waterfalls.',
        'destination': 'Nepal - Pokhara',
        'price': 699.00,
        'duration': '6 Days / 5 Nights',
        'includes': 'Flights, Lakeside Hotel, Paragliding, Boating, Tours, Breakfast'
    },
]

# World-Class Packages
world_packages = [
    {
        'name': 'Swiss Alps & Italian Lakes',
        'description': 'Discover the beauty of Switzerland and Italy. Visit Zurich, Lucerne, Interlaken, Lake Como, and Milan. Experience Alpine scenery, luxury trains, and Italian cuisine.',
        'destination': 'Switzerland & Italy',
        'price': 3899.00,
        'duration': '10 Days / 9 Nights',
        'includes': 'Flights, 4-Star Hotels, Swiss Travel Pass, Tours, Some Meals'
    },
    {
        'name': 'African Safari Experience',
        'description': 'Witness the Big Five in Kenya and Tanzania. Includes Masai Mara, Serengeti, Ngorongoro Crater, and Zanzibar beach extension. Luxury safari lodges and expert guides.',
        'destination': 'Kenya & Tanzania',
        'price': 4599.00,
        'duration': '12 Days / 11 Nights',
        'includes': 'Flights, Safari Lodges, Game Drives, Park Fees, Meals, Transfers'
    },
    {
        'name': 'New Zealand Adventure',
        'description': 'Explore both North and South Islands. Auckland, Rotorua, Queenstown, Milford Sound, and more. Adventure activities, stunning landscapes, and Maori culture.',
        'destination': 'New Zealand',
        'price': 4299.00,
        'duration': '14 Days / 13 Nights',
        'includes': 'Flights, Hotels, Car Rental, Activities, Some Meals, Tours'
    },
]

all_packages = nepal_packages + world_packages

for pkg_data in all_packages:
    package, created = Package.objects.get_or_create(
        name=pkg_data['name'],
        defaults=pkg_data
    )
    if created:
        print(f"✓ Added package: {package.name}")

# Nepal & World Deals
nepal_deals = [
    {
        'title': 'Chitwan Jungle Safari Special',
        'description': 'Explore Chitwan National Park with elephant safari, jungle walks, canoe rides, and Tharu cultural show. Stay at a jungle resort with all meals included.',
        'destination': 'Nepal - Chitwan',
        'original_price': 499.00,
        'discounted_price': 349.00,
        'discount_percentage': 30,
        'valid_until': (datetime.now() + timedelta(days=30)).date(),
        'is_active': True
    },
    {
        'title': 'Lumbini Pilgrimage Package',
        'description': 'Visit the birthplace of Lord Buddha. Includes Maya Devi Temple, Ashoka Pillar, monasteries, and meditation sessions. Peaceful spiritual journey.',
        'destination': 'Nepal - Lumbini',
        'original_price': 399.00,
        'discounted_price': 279.00,
        'discount_percentage': 30,
        'valid_until': (datetime.now() + timedelta(days=25)).date(),
        'is_active': True
    },
]

world_deals = [
    {
        'title': 'Paris & London Combo',
        'description': 'Visit two iconic cities! Includes Eiffel Tower, Louvre, Big Ben, Buckingham Palace, and Eurostar train. Perfect European getaway.',
        'destination': 'France & UK',
        'original_price': 2199.00,
        'discounted_price': 1599.00,
        'discount_percentage': 27,
        'valid_until': (datetime.now() + timedelta(days=20)).date(),
        'is_active': True
    },
    {
        'title': 'Dubai & Abu Dhabi Explorer',
        'description': 'Experience UAE luxury! Burj Khalifa, desert safari, Sheikh Zayed Mosque, Ferrari World, and shopping. 5-star hotels included.',
        'destination': 'UAE',
        'original_price': 1899.00,
        'discounted_price': 1399.00,
        'discount_percentage': 26,
        'valid_until': (datetime.now() + timedelta(days=18)).date(),
        'is_active': True
    },
]

all_deals = nepal_deals + world_deals

for deal_data in all_deals:
    deal, created = Deal.objects.get_or_create(
        title=deal_data['title'],
        defaults=deal_data
    )
    if created:
        print(f"✓ Added deal: {deal.title}")

print("\n✅ Nepal and world destinations added successfully!")
print(f"Total Flights: {Flight.objects.count()}")
print(f"Total Packages: {Package.objects.count()}")
print(f"Total Deals: {Deal.objects.count()}")
