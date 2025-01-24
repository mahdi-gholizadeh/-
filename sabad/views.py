from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import sabad, sabad_detail
from products.models import Product
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404
from .models import sabad, sabad_detail
from products.models import Product

def add_to_cart(request, product_id):
    if request.method == 'POST':

        product = get_object_or_404(Product, id=product_id)


        sabad_obj, created = sabad.objects.get_or_create(user=request.user, paid=False)


        count = int(request.POST.get('count', 1))


        sabad_item, item_created = sabad_detail.objects.get_or_create(
            order=sabad_obj,
            product=product,
            defaults={'count': count, 'price': product.price}
        )

        if not item_created:

            sabad_item.count += count
            sabad_item.save()

        return redirect('cart_detail')  



@login_required
def cart_detail(request):
    user_cart = sabad.objects.filter(user=request.user, paid=False).first()
    if not user_cart:
        user_cart = sabad.objects.create(user=request.user, paid=False)

    cart_items = sabad_detail.objects.filter(order=user_cart)
    cart_items_with_total = [
        {
            'product': item.product,
            'count': item.count,
            'price': item.price,
            'total_price': item.count * item.price,
            'id': item.id,
        }
        for item in cart_items
    ]
    total_price = sum(item['total_price'] for item in cart_items_with_total)

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items_with_total,
        'total_price': total_price,
    })



@login_required
def remove_from_cart(request, detail_id):
    cart_item = get_object_or_404(sabad_detail, id=detail_id, order__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

