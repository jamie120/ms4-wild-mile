from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product, Category
from conversions.models import CamperConversion
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    current_category = None
    sort = None
    direction = None
    all_categories = Category.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            current_category = request.GET['category']

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_category': current_category,
        'current_sorting': current_sorting,
        'all_categories': all_categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """
    product = get_object_or_404(Product, pk=product_id)
    my_listings = None
    if product.sku == '12345678':
        try:
            username = request.user.username
            profile = UserProfile.objects.get(user__username=username)
            my_listings = CamperConversion.objects.all().filter(user=profile).filter(is_active=False)
        except UserProfile.DoesNotExist:
            messages.info(request, 'Please login to view this product.')
            return redirect(reverse('products'))

    context = {
        'product': product,
        'my_listings': my_listings,
    }

    return render(request, 'products/product_detail.html', context)


def listing_levels(request):
    """ A view to show listing pricing level details """

    context = {
        'from_listing_fee_page': True,
    }

    return render(request, 'products/listing_levels.html', context)


def view_plan(request, product_id):
    my_listings = None
    product = get_object_or_404(Product, pk=product_id)
    try:
        username = request.user.username
        profile = UserProfile.objects.get(user__username=username)
        my_listings = CamperConversion.objects.all().filter(user=profile).filter(is_active=False)
    except UserProfile.DoesNotExist:
        messages.info(request, 'Please login to view this product.')
        return redirect(reverse('products'))
    context = {
        'product': product,
        'from_listing_fees_page': True,
        'my_listings': my_listings,
    }

    return render(request, 'products/product_detail.html', context)
