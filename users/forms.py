from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.backends import get_user_model
from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile


User = get_user_model()


class CreationForm(UserCreationForm):
    # phne = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Пример: +79671234455'}),
    #                             label="Номер телефона", required=False
    #                             )
    class Meta(UserCreationForm.Meta):
            model = User
            fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)
