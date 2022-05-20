from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def index(request):
    """A view to return the index page"""
    messages.add_message(request, messages.DEBUG,
                         'Salut asta este Un DEBUG Mesaj.')
    messages.add_message(request, messages.INFO,
                         'Salut asta este o informatie.')
    messages.add_message(request, messages.SUCCESS,
                         'Salut asta este o succes.')
    messages.add_message(request, messages.WARNING,
                         'Salut asta este o avertizare.')
    messages.add_message(request, messages.ERROR, 'Salut asta este o eoare.')
    return render(request, 'home/index.html')
