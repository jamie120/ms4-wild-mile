from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import CamperConversion

# Create your views here.


def all_conversions(request):
    """ A view to show all conversions,
    including sorting and search queries """

    conversions = CamperConversion.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('conversions'))

            queries = Q(name__icontains=query) | Q(conversion_description__icontains=query)
            conversions = conversions.filter(queries)

    context = {
        'conversions': conversions,
        'search_term': query,
    }

    return render(request, 'conversions/conversions.html', context)


def conversion_detail(request, conversion_id):
    """ A view to show conversion details """

    conversion = get_object_or_404(CamperConversion, pk=conversion_id)
    electrics = conversion.electrics.all()
    image_list = conversion.images.all()

    print(image_list[0])

    for image in image_list:
        print(image.image.url)

    print(electrics)

    context = {
        'conversion': conversion,
        'electrics': electrics,
        'image_list': image_list
    }

    return render(request, 'conversions/conversion_detail.html', context)
