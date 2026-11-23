from django.urls import path
from . import views
from . import api_views


app_name = 'tourism'  
urlpatterns = [
    # Web routes
    path('', views.home, name='home'),
    path('destination/<int:id>/', views.destination_details, name='details'),
    path('book/<int:id>/', views.book_package, name='book'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),  # ← ADD THIS
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
   
    # API routes
    path('api/destinations/', api_views.destination_api, name='api_destinations'),
    path('api/destinations/<int:id>/', api_views.destination_detail_api, name='api_destination_detail'),
    path('api/packages/', api_views.package_api, name='api_packages'),
    path('api/bookings/', api_views.booking_api, name='api_bookings'),
    path('api/stats/', api_views.api_stats, name='api_stats'),
]
