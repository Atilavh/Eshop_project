from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)