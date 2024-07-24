from django.urls import path
from . import views

urlpatterns = [
    path('products-list', views.ProductListView.as_view(), name='products-list'),
    path('product-favorite', views.AddFavoriteView.as_view(), name='products-favorite'),
    path('product-details/<slug:slug>', views.ProductDetailView.as_view(), name='products-details'),

]