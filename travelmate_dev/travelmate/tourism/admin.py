from django.contrib import admin
from .models import Destination, Package, Booking ,UserProfile


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """Admin interface for Destination model"""
    list_display = ['name', 'country', 'price', 'duration', 'created_at']
    list_filter = ['country', 'created_at']
    search_fields = ['name', 'country', 'description']
    readonly_fields = ['created_at', 'updated_at']
   
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'country', 'description')
        }),
        ('Details', {
            'fields': ('price', 'duration', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )




@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    """Admin interface for Package model"""
    list_display = ['title', 'destination', 'hotel_type', 'transport', 'created_at']
    list_filter = ['destination', 'created_at']
    search_fields = ['title', 'destination__name']
    readonly_fields = ['created_at']
   
    fieldsets = (
        ('Package Details', {
            'fields': ('destination', 'title')
        }),
        ('Accommodations & Transport', {
            'fields': ('hotel_type', 'transport')
        }),
        ('Package Inclusions', {
            'fields': ('inclusions',),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )




@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for Booking model"""
    list_display = ['user', 'package', 'travel_date', 'members', 'status', 'created_at']
    list_filter = ['status', 'travel_date', 'created_at']
    search_fields = ['user__username', 'package__title']
    readonly_fields = ['created_at', 'updated_at', 'user']
   
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'package')
        }),
        ('Travel Details', {
            'fields': ('travel_date', 'members')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
   
    actions = ['confirm_booking', 'cancel_booking']
   
    def confirm_booking(self, request, queryset):
        """Action to confirm bookings"""
        updated = queryset.update(status='Confirmed')
        self.message_user(request, f'{updated} booking(s) confirmed successfully.')
    confirm_booking.short_description = "Confirm selected bookings"
   
    def cancel_booking(self, request, queryset):
        """Action to cancel bookings"""
        updated = queryset.update(status='Cancelled')
        self.message_user(request, f'{updated} booking(s) cancelled.')
    cancel_booking.short_description = "Cancel selected bookings"




@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin interface for UserProfile model"""
    list_display = ['user', 'phone', 'city', 'country', 'passport_number', 'created_at']
    list_filter = ['country', 'created_at']
    search_fields = ['user__username', 'phone', 'passport_number']
    readonly_fields = ['created_at', 'updated_at']
   
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('phone', 'date_of_birth', 'gender', 'nationality', 'passport_number')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'country', 'zip_code')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
