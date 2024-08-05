from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'shared/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'this is data'
        context['message'] = 'this is message'
        return context

# def index_page(request):
#     return render(request, 'shared/index.html')


def header_partial(request):
    return render(request, 'header_render_partial/header_partial.html')


def footer_partial(request):
    return render(request, 'footer_render_partial/footer_partial.html')


