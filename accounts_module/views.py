from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.http import Http404
from accounts_module.forms import RegistrationForm, LoginForm, ForgotForm
from django.urls import reverse
from accounts_module.models import User
from django.http import HttpResponse, HttpResponseRedirect


def Register(request):
    register = RegistrationForm(request.POST)
    if register.is_valid():
        user_email = register.cleaned_data['email']
        user_password = register.cleaned_data['password']
        user: bool = User.objects.filter(email__iexact=user_email).exists()
        if user:
            register.add_error('email', 'این ایمیل قبلا ثبت شده')
        else:
            new_user = User(
                email=user_email,
                email_active_code=get_random_string(48),
                is_active=False,
                username=user_email
            )
            new_user.set_password(user_password)
            new_user.save()
            return redirect(reverse('Home-page'))
    context = {
        'register': register
    }
    return render(request, 'Accounts/register_page.html', context)


def confirm_register(request, email_active_code):
    user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
    if user is not None:
        if not user.is_active:
            user.is_active = True,
            user.email_active_code = get_random_string(48),
            user.save()
            return redirect(reverse('Home-page'))
        else:
            pass

        raise Http404


def login(request: object) -> object:
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        user_email = login_form.cleaned_data.get('email')
        user_password = login_form.cleaned_data.get('password')
        user: User = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            if not user.is_active:
                login_form.add_error('email', 'حساب کاربری شما فعال نمی باشد')
            else:
                is_password_correct = user.check_password(user_password)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('Home-page'))
                else:
                    login_form.add_error('email', 'ایمیل یا کلمه عبور صحیح نمی باشد')
    else:
        login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }

    return render(request, 'Accounts/login_page.html', context)


def forgot_pass(request):
    ForgetPage = ForgotForm(request.POST)
    if ForgetPage.is_valid():
        user_email = ForgetPage.cleaned_data.get('email')
        user: User = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            pass
    context = {
        'ForgetPage': ForgetPage
    }

    return render(request, 'Accounts/forgot_pass_page.html', context)


def ResetPassword(request):
    reset = ForgotForm(request.POST)
    if reset.is_valid():
        user_email = reset.cleaned_data.get('email')
        user: User = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            pass
    context = {
        'reset': reset
    }

    return render(request, 'Accounts/forgot_pass_page.html', context)
