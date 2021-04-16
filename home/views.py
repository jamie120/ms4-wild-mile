from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the index page """
    return render(request, 'home/about.html')


def faq(request):
    """ A view to return the index page """
    return render(request, 'home/faq.html')


def page_not_found(request, *args, **argv):
    return render(request, 'home/404.html')


def server_error(request, *args, **argv):
    return render(request, 'home/500.html')


def permission_denied(request, *args, **argv):
    return render(request, 'home/403.html')


def bad_request(request, *args, **argv):
    return render(request, 'home/400.html')
