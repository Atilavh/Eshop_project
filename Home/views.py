from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'shared/index.html')


def header_partial(request):
    return render(request, 'header_render_partial/header_partial.html')


def footer_partial(request):
    return render(request, 'footer_render_partial/footer_partial.html')
