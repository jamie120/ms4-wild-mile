from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import CamperConversion, Category

# Create your views here.


def all_conversions(request):
    """ A view to show all conversions,
    including sorting and search queries """

    conversions = CamperConversion.objects.all()
    query = None
    sort = None
    direction = None
    categories = None
    all_categories = Category.objects.all()
    current_category = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('conversions'))

            queries = Q(name__icontains=query) | Q(conversion_description__icontains=query)
            conversions = conversions.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                conversions = conversions.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            conversions = conversions.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            conversions = conversions.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            current_category = request.GET['category']
            current_category = current_category.replace("_", " ").capitalize()

    current_sorting = f'{sort}_{direction}'

    context = {
        'conversions': conversions,
        'search_term': query,
        'current_categories': categories,
        'current_category': current_category,
        'all_categories': all_categories,
        'current_sorting': current_sorting,
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
