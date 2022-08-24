from email.policy import default
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

def contact(request):
    superusers_emails = settings.DEFAULT_FROM_EMAIL
    print(superusers_emails)
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [superusers_emails])

            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect("thanks")
    return render(request, "contact/contact.html", {"form": form})

def thanks(request):

    return render(request, 'contact/succes.html')