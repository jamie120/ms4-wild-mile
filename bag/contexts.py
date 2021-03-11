from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    grand_total = 0
    bag = request.session.get('bag', {})
    listing_uuid = None

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            if product.sku != '12345678':
                for size, quantity in item_data['items_by_size'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })
            else:
                for listing_uuid, listing_uuid in item_data['item_with_uuid'].items():
                    total += 1 * product.price
                    product_count = 1
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': 1,
                        'product': product,
                        'listing_uuid': listing_uuid,
                    })
    # Check if bag is 0.00 and remove delivery charge, to allow checkout of promotional listing fees without delivery charges.
    if total == 0:
        delivery = 0
        free_delivery_delta = 0
    elif total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if bag_items:
        grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'listing_uuid': listing_uuid,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
