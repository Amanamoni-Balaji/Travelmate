from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination, Package, Booking
from .serializers import DestinationSerializer, PackageSerializer, BookingSerializer




@api_view(['GET'])
def destination_api(request):
    """Get all destinations - API endpoint"""
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
   
    return Response({
        'success': True,
        'data': serializer.data,
        'count': len(serializer.data)
    })




@api_view(['GET'])
def destination_detail_api(request, id):
    """Get specific destination - API endpoint"""
    try:
        destination = Destination.objects.get(id=id)
        serializer = DestinationSerializer(destination)
       
        return Response({
            'success': True,
            'data': serializer.data
        })
    except Destination.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Destination not found'
        }, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def package_api(request):
    """Get all packages - API endpoint"""
    destination_id = request.query_params.get('destination_id', None)
   
    if destination_id:
        packages = Package.objects.filter(destination_id=destination_id)
    else:
        packages = Package.objects.all()
   
    serializer = PackageSerializer(packages, many=True)
   
    return Response({
        'success': True,
        'data': serializer.data,
        'count': len(serializer.data)
    })




@api_view(['GET'])
def booking_api(request):
    """Get user bookings - API endpoint"""
    if not request.user.is_authenticated:
        return Response({
            'success': False,
            'message': 'Authentication required'
        }, status=status.HTTP_401_UNAUTHORIZED)
   
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
   
    return Response({
        'success': True,
        'data': serializer.data,
        'count': len(serializer.data)
    })




@api_view(['GET'])
def api_stats(request):
    """Get API statistics - API endpoint"""
    stats = {
        'total_destinations': Destination.objects.count(),
        'total_packages': Package.objects.count(),
        'total_bookings': Booking.objects.count(),
        'pending_bookings': Booking.objects.filter(status='Pending').count(),
        'confirmed_bookings': Booking.objects.filter(status='Confirmed').count(),
    }
   
    return Response({
        'success': True,
        'data': stats
    })