from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm
from django import forms
from captcha.fields import ReCaptchaField


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class CustomLoginForm(LoginForm):
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CustomLoginForm, self).save(request)
        user.save()
        return user
