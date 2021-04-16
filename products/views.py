from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from conversions.models import CamperConversion
from .forms import ProductForm
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    products = products.exclude(sku='12345678')  # Remove listing token from displaying on merchandise page
    current_category = None
    sort = None
    direction = None
    query = None
    all_categories = Category.objects.all()
    all_categories = all_categories.exclude(name='listing_fee')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query)
            products = products.filter(queries)

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
            # Find 'inactive' listings associated to user
            my_listings = CamperConversion.objects.all().filter(user=profile).filter(is_active=False)
        except UserProfile.DoesNotExist:
            messages.info(request, 'Please login to view this product.')
            return redirect(reverse('listing_levels'))

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
        # Find 'inactive' listings associated to user
        my_listings = CamperConversion.objects.all().filter(user=profile).filter(is_active=False)
    except UserProfile.DoesNotExist:
        messages.info(request, 'Please login to view this product.')
        return redirect(reverse('listing_levels'))
    context = {
        'product': product,
        'from_listing_fees_page': True,
        'my_listings': my_listings,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admin can add products')
        return redirect(reverse('home'))
    else:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request,
                                 "Product added successfully")
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product.')

        else:
            form = ProductForm()

        template = 'products/add_product.html'
        context = {
            'form': form,
        }
        return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admin can edit products')
        return redirect(reverse('home'))
    else:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, f'Successfully updated {product.name}!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update product. Please ensure the form is valid')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are editing {product.name}')

        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
        }
        return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
