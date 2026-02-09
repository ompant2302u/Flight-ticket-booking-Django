from django.contrib import admin
from .models import Flight, Package, Deal, Ticket, Profile, PackageBooking, DealBooking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "airline",
        "flight_number",
        "origin",
        "destination",
        "departure_date",
        "price",
        "seats_available",
    )

    list_filter = (
        "airline",
        "origin",
        "destination",
        "departure_date",
    )

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price', 'duration', 'created_at']
    search_fields = ['name', 'destination']

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'discounted_price', 'discount_percentage', 'valid_until', 'is_active']
    list_filter = ['is_active', 'valid_until']
    search_fields = ['title', 'destination']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_id', 'passenger_name', 'flight', 'status', 'booked_at']
    list_filter = ['status', 'payment_status', 'booked_at']
    search_fields = ['ticket_id', 'passenger_name', 'email']

@admin.register(PackageBooking)
class PackageBookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'customer_name', 'package', 'travelers', 'status', 'booked_at']
    list_filter = ['status', 'booked_at']
    search_fields = ['booking_id', 'customer_name', 'email']

@admin.register(DealBooking)
class DealBookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'customer_name', 'deal', 'status', 'booked_at']
    list_filter = ['status', 'booked_at']
    search_fields = ['booking_id', 'customer_name', 'email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    search_fields = ['user__username', 'phone']
