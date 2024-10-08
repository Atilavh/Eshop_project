from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory
from django.views.generic import ListView, DetailView, View
from django.views.generic.base import TemplateView


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 2

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        # data = base_query.filter(is_active=True)
        return base_query


class ProductDetailView(DetailView):
    template_name = 'Products/product-details.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_products = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorite')
        context['is_favorite'] = favorite_product_id == str(loaded_products.id)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data()
    #     slug = kwargs['slug']
    #     product = get_object_or_404(Product, slug=slug)
    #     context['product'] = product
    #     return context


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'Products/product-details.html', {
# #         'products': product
#     })

# def products_list(request):
#     product_list = Product.objects.all().order_by('price')[:5]
#     return render(request, 'Products/products_list.html', {
#         'product_list': product_list,
#     })
class AddFavoriteView(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorite'] = product_id
        return redirect(product.get_absolute_url())
