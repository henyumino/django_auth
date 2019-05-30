from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from . import forms


def welcome(request):
    return render(request,'welcome.html')

@login_required
def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # send_mail(
            #     'dari kontak website',
            #     request.POST['subject'],
            #     request.POST['email'],
            #     ['fr@fr.fr'],
            #     fail_silently=False,
            # )

            messages.success(request,'berhasil kirim email')
            return HttpResponseRedirect(reverse('contact'))

    return render(request,'contact.html',{'form':form})