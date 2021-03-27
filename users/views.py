from django.urls import reverse_lazy
from django.views.generic import CreateView
import datetime as dt
from .forms import CreationForm, ProfileForm
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.conf import settings


def singup(request):
    if request.method == 'POST':
        user_form = CreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and request.recaptcha_is_valid:
            user_form.save()
            profile_form.save()
            return redirect('index')

    else:
        user_form = CreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

    return render(request, 'signup.html',
        {'user_form': user_form, 'profile_form': profile_form, 'GOOGLE_RECAPTCHA_SECRET_KEY': settings.GOOGLE_RECAPTCHA_SECRET_KEY},
        )