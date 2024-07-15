from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.db.models import Avg, Max, Min


def products_list(request):
    product_list = Product.objects.all().order_by('price')[:5]
    return render(request, 'Products/products_list.html', {
        'product_list': product_list,
    })


# def ProductDetailView(request, slug):
#     # try:
#     #     product = product.objects.get(id=product_id)
#     # except:
#     #     raise Http404
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'Products_detail/Products_detail.html', {
#         'products': product
#     })
