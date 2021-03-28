from .forms import CreationForm, ProfileForm
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


def singup(request):
    """Регистрация"""
    if request.method == 'POST':
        user_form = CreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and request.recaptcha_is_valid:
            user_form.save()
            phone = profile_form.cleaned_data.get('phone')
            user = User.objects.get(username=user_form.cleaned_data.get('username'))
            user.profile.phone = phone
            user.save()
            return redirect('index')

    else:
        user_form = CreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

    return render(request, 'signup.html',
        {'user_form': user_form,
         'profile_form': profile_form,
         'GOOGLE_RECAPTCHA_SECRET_KEY': settings.GOOGLE_RECAPTCHA_SECRET_KEY
         })
