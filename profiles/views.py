from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, SavedListings
from .forms import UserProfileForm
from conversions.models import CamperConversion

from checkout.models import Order


@login_required
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
    username = request.user.username
    profile = UserProfile.objects.get(user__username=username)
    saved_listings = SavedListings.objects.all().filter(user=profile)
    template = 'profiles/saved_listings.html'
    context = {
        'saved_listings': saved_listings,
    }

    return render(request, template, context)


def my_listings(request):
    """ Display the users conversion listings """
    username = request.user.username
    profile = UserProfile.objects.get(user__username=username)
    my_listings = CamperConversion.objects.all().filter(user=profile)
    template = 'profiles/my_listings.html'
    context = {
        'my_listings': my_listings,
    }

    return render(request, template, context)


def view_order_history(request):
    """ Display the users order_history """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/view_order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display a particular order detail by
    rendering it on the checkout success page """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def message_portal(request):
    """ Displays a coming soon message, as this is a future feature """

    template = 'profiles/message_portal.html'
    context = {}

    return render(request, template, context)
