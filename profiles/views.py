from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user profile page """

    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
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

    template = 'profiles/order_history.html'
    context = {}

    return render(request, template, context)


def message_portal(request):
    """ Displays a coming soon message, as this is a future feature """

    template = 'profiles/message_portal.html'
    context = {}

    return render(request, template, context)
