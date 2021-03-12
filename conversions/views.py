from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.forms import modelformset_factory

from .models import CamperConversion, Category, PostImage
from .forms import ConversionForm, ImageForm
from profiles.models import SavedListings, UserProfile

# Create your views here.


def all_conversions(request):
    """ A view to show all conversions,
    including sorting and search queries """

    # Filter only listings that are active
    conversions = CamperConversion.objects.all().filter(is_active=True)

    query = None
    sort = None
    direction = None
    current_category_css_check = None
    all_categories = Category.objects.all()
    current_category = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('conversions'))

            queries = Q(listing_title__icontains=query) | Q(conversion_description__icontains=query)

            # Filter conversions with search term and is_active
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
            current_category = request.GET['category']
            current_category_css_check = current_category
            current_category = current_category.replace("_", " ").capitalize()

    current_sorting = f'{sort}_{direction}'

    context = {
        'conversions': conversions,
        'search_term': query,
        'current_category': current_category,
        'current_category_css_check': current_category_css_check,
        'all_categories': all_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'conversions/conversions.html', context)


def conversion_detail(request, conversion_id):
    """ A view to show conversion details """

    conversion = get_object_or_404(CamperConversion, pk=conversion_id)
    electrics = conversion.electrics.all()
    image_list = conversion.images.all()

    for image in image_list:
        print(image.image.url)

    context = {
        'conversion': conversion,
        'electrics': electrics,
        'image_list': image_list
    }

    return render(request, 'conversions/conversion_detail.html', context)


@login_required
def add_conversion(request):
    """ Add a conversion request to the admin """
    ImageFormSet = modelformset_factory(PostImage, form=ImageForm, extra=3)

    if request.method == 'POST':

        form = ConversionForm(request.POST, request.FILES)
        print(form)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
        if form.is_valid() and formset.is_valid():
            post_form = form.save(commit=False)
            user = request.user.id
            user = get_object_or_404(UserProfile, pk=user)
            post_form.user = user
            post_form.save()
            form.save_m2m()

            for form in formset.cleaned_data:
                if 'image' in form:
                    image = form['image']
                    photo = PostImage(conversion=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Posted!")
            return redirect(reverse('conversion_detail', args=[post_form.id]))
        else:
            messages.error(request, 'Failed to submit form.')

    else:
        form = ConversionForm()
        formset = ImageFormSet(queryset=PostImage.objects.none())

    template = 'conversions/add_conversion.html'
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, template, context)


@login_required
def edit_conversion(request, conversion_id):
    """ Edit a conversion in the database """
    ImageFormSet = modelformset_factory(PostImage, form=ImageForm, extra=3)
    conversion = get_object_or_404(CamperConversion, pk=conversion_id)

    # Check if listing is currently active
    previously_active = conversion.is_active

    if request.method == 'POST':
        form = ConversionForm(request.POST, request.FILES, instance=conversion)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.filter(conversion__pk=conversion_id))
        data = PostImage.objects.filter(conversion=conversion)
        if form.is_valid and formset.is_valid():
            post_form = form.save(commit=False)

            # Set is_active according to previous state
            if previously_active:
                post_form.is_active = True
                post_form.save()
                form.save_m2m()
            else:
                print(post_form.electrics)
                post_form.save()
                form.save_m2m()

            # Check if new photos are to replace exisiting photos, delete and update as required.
            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        pic = PostImage(conversion=post_form, image=f.cleaned_data.get('image')) 
                        pic.save()
                    elif request.POST.get('form-'+str(index)+'-DELETE') is not None:
                        pic = PostImage.objects.get(id=request.POST.get('form-'+str(index)+'-id'))
                        pic.delete()
                    else:
                        pic = PostImage(conversion=post_form, image=f.cleaned_data.get('image'))

                        d = PostImage.objects.get(id=data[index].id)  # get slide id which was uploaded
                        d.image = pic.image  # changing the database title with new title

                        d.save()
            messages.success(request, f'Succesfully updated listing : {conversion.listing_title}')
            return redirect(reverse('conversion_detail', args=[conversion.id]))
        else:
            messages.error(request, 'Failed to update the listing. Please ensure the form is valid')
            return redirect(reverse('conversion_detail', args=[conversion.id]))
    else:
        # Check if the listing author is the current user
        if request.user == conversion.user.user:
            form = ConversionForm(instance=conversion)
            formset = ImageFormSet(queryset=PostImage.objects.filter(conversion__pk=conversion_id))
            messages.info(request, f'You are editing {conversion.listing_title}')
        else:
            messages.error(request, 'Sorry, you can only edit listings which you have created previously.')
            return redirect(reverse('my_listings'))
    template = 'conversions/edit_conversion.html'
    context = {
        'form': form,
        'formset': formset,
        'conversion': conversion,
    }

    return render(request, template, context)


@login_required
def delete_conversion(request, conversion_id):
    """ Delete a conversion listing """
    conversion = get_object_or_404(CamperConversion, pk=conversion_id)

    # Check if the listing author is the current user
    if request.user == conversion.user.user:
        conversion.delete()
        messages.success(request, 'Listing successfully deleted')
        return redirect(reverse('my_listings'))
    else:
        messages.error(request, 'Sorry, you can only delete listings which you have created previously.')
        return redirect(reverse('my_listings'))


@login_required
def approve_conversions(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admin can approve conversions')
        return redirect(reverse('home'))

    conversions = CamperConversion.objects.all()
    require_approval = conversions.filter(is_active=False).exists()
    print(require_approval)
    template = 'conversions/approve_conversions.html'
    context = {
        'conversions': conversions,
        'require_approval': require_approval,
    }
    return render(request, template, context)


@login_required
def manage_conversions(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admin can manage conversions')
        return redirect(reverse('home'))

    conversions = CamperConversion.objects.all()
    live_listings = conversions.filter(is_active=True)
    require_approval = conversions.filter(is_active=False).exists()
    pending_approval_listings = conversions.filter(is_active=False)
    template = 'conversions/manage_conversions.html'
    context = {
        'conversions': conversions,
        'require_approval': require_approval,
        'live_listings': live_listings,
        'pending_approval_listings': pending_approval_listings,
    }
    return render(request, template, context)


@login_required
def approve_conversion(request, conversion_id):
    """ Function change the active status of a conversion listing in the store """
    try:
        conversion = get_object_or_404(CamperConversion, pk=conversion_id)
        conversion.is_active = True
        conversion.save()
        return redirect(reverse('approve_conversions'))
    except UnboundLocalError:
        messages.error(request, 'Failed to approve listing')
        return redirect(reverse('approve_conversions'))


@login_required
def delist_conversion(request, conversion_id):
    """ Function change the active status of a conversion listing in the store """
    try:
        conversion = get_object_or_404(CamperConversion, pk=conversion_id)
        conversion.is_active = False
        conversion.save()
        return redirect(reverse('manage_conversions'))
    except UnboundLocalError:
        messages.error(request, 'Failed to delist listing')
        return redirect(reverse('manage_conversions'))


@login_required
def save_listing(request, conversion_id, conversion_unique_ref):
    """
    Save a conversion to the user profile
    """
    if request.user.is_authenticated:
        username = request.user.username
        profile = UserProfile.objects.get(user__username=username)
        all_saved_items = SavedListings.objects.all().filter(user=profile)
        if all_saved_items:
            add_item = True
            for item in all_saved_items:
                print(type(conversion_unique_ref))
                print(type(item.conversion.unique_ref))
                if str(conversion_unique_ref) == str(item.conversion.unique_ref):
                    add_item = False

            if add_item:
                messages.info(request, 'Listing added to your profile')
                saved_item = SavedListings(user=profile, conversion_id=conversion_id, status=True)
                saved_item.save()
                return HttpResponseRedirect(reverse('conversion_detail', args=(conversion_id,)))
            else:
                messages.info(request, 'You already have this listing saved to your profile')
                return HttpResponseRedirect(reverse('conversion_detail', args=(conversion_id,)))

        else:
            print("No items in profile, first item added")
            messages.info(request, 'Congratulations, you saved your first listing to your profile')
            saved_item = SavedListings(user=profile, conversion_id=conversion_id, status=True)
            saved_item.save()
            return HttpResponseRedirect(reverse('conversion_detail', args=(conversion_id,)))
    else:
        print("User not logged in")
        return HttpResponseRedirect(reverse('conversion_detail', args=(conversion_id,)))
    # get username
    # get profile
    # save conversion id to savelistings in the user profile   profile.saved_lisings.name = conversion_id
    # redirect to profile/saved listings page