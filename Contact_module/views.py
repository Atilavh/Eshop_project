from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


# Create your views here.

def contact_us_page(request):
    # if request.method == 'POST':
    #     print(request.POST['email'])
    #     print(request.POST['name'])
    #     print(request.POST['subject'])
    #     print(request.POST['message'])
    #     return redirect(reverse('Home-page'))
    # contact_form = ContactForm(request.POST or None)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('Home-page')
    else:
        contact_form = ContactForm()
    return render(request, 'contact_page/contact-us.html', {
        'contact_form': contact_form
    })
