from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('flights/', views.flights_view, name='flights'),
    path('flight/book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('packages/', views.packages_view, name='packages'),
    path('package/book/<int:package_id>/', views.book_package, name='book_package'),
    path('deals/', views.deals_view, name='deals'),
    path('deal/book/<int:deal_id>/', views.book_deal, name='book_deal'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('api/autocomplete/destinations/', views.autocomplete_destinations, name='autocomplete_destinations'),
    path('api/autocomplete/airlines/', views.autocomplete_airlines, name='autocomplete_airlines'),
    path('ticket/<uuid:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<uuid:ticket_id>/refund/', views.request_refund, name='request_refund'),
    path('package/<uuid:booking_id>/', views.package_detail, name='package_detail'),
    path('deal/<uuid:booking_id>/', views.deal_detail, name='deal_detail'),
]
