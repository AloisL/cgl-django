from django import forms
from django.contrib.auth.forms import UserCreationForm

from mopga.modules.user.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    # TODO : Ajouter type utilisateur

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
