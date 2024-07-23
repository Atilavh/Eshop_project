from django import forms
from .models import Contact_us


# class ContactForm(forms.Form):
#     fullname = forms.CharField(
#         max_length=50,
#         label='نام کامل',
#         error_messages={
#             'required': 'لطفا فیلد نام رو درست پر کن',
#             'max_length': 'بیشتر از 50 کاراکتر پر نکن'
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'نام و نام خانوادگی'
#         })
#     )
#     email = forms.EmailField(
#         label='ایمیل',
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'ایمیل'
#         })
#     )
#     subject = forms.CharField(
#         label='عنوان',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'موضـوع',
#             'name': 'subject'
#         })
#     )
#     message = forms.CharField(
#         label='متن تماس با ما',
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'پیغـام شمـا',
#             'id': 'message'
#         })
#     )
#

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['title', 'email', 'full_name', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        },
        error_messages = {
            'required': 'لطفا فیلد نام رو درست پر کن',
            'max_length': 'بیشتر از 50 کاراکتر پر نکن'
        }


class ProfilePhotoForm(forms.Form):
    user_image = forms.ImageField(widget=forms.FileInput())
