import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')
django.setup()

from myApp.models import Flight

print("Updating flight types...")

# Domestic routes (within same country or short distances)
domestic_keywords = ['Kathmandu', 'Pokhara', 'Lukla', 'Bharatpur', 'Jomsom']

for flight in Flight.objects.all():
    # Check if both origin and destination contain domestic keywords
    is_domestic = any(keyword in flight.origin for keyword in domestic_keywords) and \
                  any(keyword in flight.destination for keyword in domestic_keywords)
    
    if is_domestic:
        flight.flight_type = 'domestic'
    else:
        flight.flight_type = 'international'
    
    flight.save()
    print(f"✓ {flight.flight_number}: {flight.get_flight_type_display()}")

print("\n✅ Flight types updated successfully!")
print(f"Domestic flights: {Flight.objects.filter(flight_type='domestic').count()}")
print(f"International flights: {Flight.objects.filter(flight_type='international').count()}")
