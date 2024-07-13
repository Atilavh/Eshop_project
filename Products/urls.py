from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView, name='List'),
    path('product-detail/<slug:slug>', views.ProductDetailView, name='Detail'),
]
