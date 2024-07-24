from django import forms


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