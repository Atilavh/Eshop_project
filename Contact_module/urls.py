from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contact_us_page, name='contact-us'),
    path('', views.ContactUsView.as_view(), name='contact-us'),
    path('create-profile', views.upload_file, name='upload'),
]
