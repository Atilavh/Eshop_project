from django.urls import path
from . import views

urlpatterns = [
    path('CreateAccount', views.Register, name='RegisterForm'),
]