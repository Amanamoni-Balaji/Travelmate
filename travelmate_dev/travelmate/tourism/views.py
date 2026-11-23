# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Destination, Package, Booking ,UserProfile
from .forms import BookingForm, RegisterForm, LoginForm ,UserProfileForm
 




def home(request):
    """Home page showing all destinations"""
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
        'page_title': 'Home'
    }
    return render(request, 'home.html', context)




def destination_details(request, id):
    """Destination details page with packages"""
    destination = get_object_or_404(Destination, id=id)
    packages = Package.objects.filter(destination=destination)
   
    context = {
        'destination': destination,
        'packages': packages,
        'page_title': destination.name
    }
    return render(request, 'details.html', context)




@login_required(login_url='tourism:login')
def book_package(request, id):
    """Book a package"""
    package = get_object_or_404(Package, id=id)
   
    if request.method == 'POST':
        form = BookingForm(request.POST)
       
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.save()
           
            messages.success(request, f'Package booked successfully! Booking ID: {booking.id}')
            return redirect('tourism:dashboard')
    else:
        form = BookingForm()
   
    context = {
        'form': form,
        'package': package,
        'page_title': 'Book Package'
    }
    return render(request, 'booking.html', context)




@login_required(login_url='tourism:login')
def dashboard(request):
    """User dashboard showing all bookings"""
    bookings = Booking.objects.filter(user=request.user)
   
    context = {
        'bookings': bookings,
        'page_title': 'My Dashboard'
    }
    return render(request, 'dashboard.html', context)




def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('tourism:home')
   
    if request.method == 'POST':
        form = RegisterForm(request.POST)
       
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
               
                messages.success(request, 'Registration successful! Please login.')
                return redirect('tourism:login')
            except Exception as e:
                messages.error(request, f'Error during registration: {str(e)}')
    else:
        form = RegisterForm()
   
    context = {
        'form': form,
        'page_title': 'Register'
    }
    return render(request, 'register.html', context)




def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('tourism:home')
   
    if request.method == 'POST':
        form = LoginForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
           
            user = authenticate(request, username=username, password=password)
           
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.username}!')
                return redirect('tourism:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
   
    context = {
        'form': form,
        'page_title': 'Login'
    }
    return render(request, 'login.html', context)




def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('tourism:home')




def contact_view(request):
    """Contact page"""
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)






@login_required(login_url='tourism:login')
def profile_view(request):
    """User profile view"""
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
   
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('tourism:profile')
    else:
        form = UserProfileForm(instance=profile)
   
    context = {
        'form': form,
        'profile': profile,
        'page_title': 'My Profile'
    }
    return render(request, 'profile.html', context)