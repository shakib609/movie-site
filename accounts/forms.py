from django import forms
from django.contrib.auth.forms import UserCreationForm as DUserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(DUserCreationForm):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
        label="Enter Password")

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
