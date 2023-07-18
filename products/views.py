from django.shortcuts import render, redirect
from products.models import Product

def get_products(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product, 'count': request.user.profile.get_cart_count()}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_be_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            # print(price)
        return render(request, 'product/products.html', context = context)

    except Exception as e:
        print(e)
    
    