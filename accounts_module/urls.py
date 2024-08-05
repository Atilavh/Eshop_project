from django.urls import path
from . import views

urlpatterns = [
    path('CreateAccount', views.Register, name='RegisterForm'),
    path('LoginPage', views.login, name='LoginForm'),
    path('ForgotPage', views.forgot_pass, name='ForgotPage'),
    path('RestePassword/<active_code>', views.forgot_pass, name='ForgotPage'),
    path('activatecode/<str:email_active_code>', views.confirm_register, name='email_active_code'),
]