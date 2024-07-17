from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='Home-page'),

    # Django_render_partial_URLS {
    # path('header-site', views.header_partial, name='header_partial'),
    # path('footer-site', views.footer_partial, name='footer_partial')
    # Django_render_partial_URLS }
]
