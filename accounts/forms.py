from django.contrib.auth.forms import UserCreationForm as DUserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(DUserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
