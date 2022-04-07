from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """Displays user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form,
    }

    return render(request, template, context)

def profile_orders(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile_orders.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)
