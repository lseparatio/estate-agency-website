from django.shortcuts import render
from django.contrib import messages

# Create your views here.


from accounts.forms import CustomSignupForm
from accounts.forms import CustomLoginForm

form_singup = CustomSignupForm()
form_login = CustomLoginForm()


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html', {'form': form_singup, 'form_login': form_login})
