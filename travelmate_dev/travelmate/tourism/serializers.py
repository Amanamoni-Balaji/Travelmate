from rest_framework import serializers
from .models import Destination, Package, Booking




class DestinationSerializer(serializers.ModelSerializer):
    """Serializer for Destination model"""
   
    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'description', 'image', 'price', 'duration', 'created_at']




class PackageSerializer(serializers.ModelSerializer):
    """Serializer for Package model"""
    destination_name = serializers.CharField(source='destination.name', read_only=True)
   
    class Meta:
        model = Package
        fields = ['id', 'destination', 'destination_name', 'title', 'hotel_type', 'transport', 'inclusions', 'created_at']




class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    user_name = serializers.CharField(source='user.username', read_only=True)
    package_title = serializers.CharField(source='package.title', read_only=True)
   
    class Meta:
        model = Booking
        fields = ['id', 'user', 'user_name', 'package', 'package_title', 'travel_date', 'members', 'status', 'created_at']