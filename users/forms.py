from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
