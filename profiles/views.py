from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'on_profile_page': True,
    }

    return render(request, template, context)


def saved_listings(request):
    """ Display the users saved listings """

    template = 'profiles/saved_listings.html'
    context = {}

    return render(request, template, context)


def my_listings(request):
    """ Display the users conversion listings """

    template = 'profiles/my_listings.html'
    context = {}

    return render(request, template, context)


def order_history(request):
    """ Display the users order_history """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def message_portal(request):
    """ Displays a coming soon message, as this is a future feature """

    template = 'profiles/message_portal.html'
    context = {}

    return render(request, template, context)
