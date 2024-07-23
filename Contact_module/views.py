from django.shortcuts import render, redirect

from Products.models import Product
from .models import Profile_Picture
from .forms import ContactUsModelForm, ProfilePhotoForm
from django.views.generic.edit import CreateView
from django.views.generic import View


class ContactUsView(CreateView):
    template_name = 'contact_page/contact-us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    # def save_images(file):
    #     with open('tmp/image.jpg', 'wb+') as dest:
    #         for chunk in file,chunks():
    #             dest.write(chunk)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     redirect('Home-page')
    #     return super().form_invalid(form)

    # def get(self, request):
    #     contact_form = ContactUsModelForm()
    #     return render(request, 'contact_page/contact-us.html', {
    #         'contact_form': contact_form
    #     })
    #
    # def post(self, request):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #         contact_form.save()
    #         return redirect('Home-page')
    #
    #     return render(request, 'contact_page/contact-us.html', {
    #         'contact_form': contact_form
    #     })


# Create your views here.

# def contact_us_page(request):
# if request.method == 'POST':
#     print(request.POST['email'])
#     print(request.POST['name'])
#     print(request.POST['subject'])
#     print(request.POST['message'])
#     return redirect(reverse('Home-page'))
# contact_form = ContactForm(request.POST or None)
# if request.method == 'POST':
# contact_form = ContactUsModelForm(request.POST)
# if contact_form.is_valid():
#         # print(contact_form.cleaned_data)
#         contact = Contact_us(
#             title=contact_form.cleaned_data.get('subject'),
#             email=contact_form.cleaned_data.get('email'),
#         #             full_name=contact_form.cleaned_data.get('full_name'),
#             message=contact_form.cleaned_data.get('message'),
#         )
# contact_form.save()
#         return redirect('Home-page')
#     else:
#         contact_form = ContactUsModelForm()
# contact_form = ContactUsModelForm()
#     return render(request, 'contact_page/contact-us.html', {
#         'contact_form': contact_form
#     })


def upload_file(request):
    form = ProfilePhotoForm()
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile_Picture(image=request.FILES['image'])
            profile.save()
            return redirect('upload')

    return render(request, 'profile.html', {
        'form': form
    })


class UploadFileView(CreateView):
    template_name = 'profile.html'
    model = Profile_Picture
    fields = '__all__'
    success_url = 'contact-us/create-profile'

