from django.urls import path
from . import views

urlpatterns = [
    path('products-list', views.products_list, name='products-list'),
    # path('products-details/<slug:slug>', views.ProductDetailView, name='Detail'),
]