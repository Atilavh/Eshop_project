from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts_module.forms import RegistrationForm


def Register(request):
    register = RegistrationForm(request.POST)
    if register.is_valid():
        print(register.cleaned_data)
    context = {
        'register': register
    }
    return render(request, 'RegisterPage/register_page.html', context)
