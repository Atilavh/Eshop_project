from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput
    )

    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label='تایید کلمه عبور',
        widget=forms.PasswordInput
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور باهم مغایرت دارد')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='پسوورد',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )


class Sing_up(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
    )
    confirm_password = forms.CharField(
        label='confirm_password',
        widget=forms.PasswordInput(),
    )