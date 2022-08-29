from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-1 profile-form-input'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-1 profile-form-input'}), required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control mb-1 profile-form-input"}), required=True)
    captcha = ReCaptchaField()
