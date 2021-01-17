from django import forms
from django.contrib.auth.forms import UserCreationForm

from mopga.modules.user.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 2}),
                                  help_text='Write here a description of your project (200 caracters max.)');
    CHOICES = [('', 'Pick a role...'), (1, 'Maker'), (2, 'Funder'), (3, 'Rater')]
    role = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    email = forms.EmailField(max_length=254)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'role', 'description')
