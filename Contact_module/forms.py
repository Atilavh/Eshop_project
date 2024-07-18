from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        max_length=50,
        label='نام کامل',
        error_messages={
            'required': 'لطفا فیلد نام رو درست پر کن',
            'max_length': 'بیشتر از 50 کاراکتر پر نکن'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        })
    )
    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضـوع',
            'name': 'subject'
        })
    )
    message = forms.CharField(
        label='متن تماس با ما',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'پیغـام شمـا',
            'id': 'message'
        })
    )
