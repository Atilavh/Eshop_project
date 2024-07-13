from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.db.models import Avg, Max, Min


def ProductListView(request):
    # console = ProductCategory(title='پلی استیشن', url='playstation')
    # console.save()
    #
    # ps_4 = Product(title='playstation4', price=14000000, is_active=True, rating=4, short_description='best console', category=console)
    # ps_4.save()

    product_list = Product.objects.all().order_by('title')
    count = product_list.count()
    avg_rating = product_list.aggregate(Avg('rating'), Min('price'), Max('rating'))
    return render(request, 'Products/Products.html', {
        'product_list': product_list,
        'products_count': count,
        'Product_avg': avg_rating
    })


def ProductDetailView(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'Products_detail/Products_detail.html', {
        'products': product
    })
