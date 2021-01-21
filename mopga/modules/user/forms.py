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


class UpdateForm(forms.Form):
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 2}),
                                  help_text='Write here a description of your project (200 caracters max.)');
    CHOICES = [('', 'Pick a role...'), (1, 'Maker'), (2, 'Funder'), (3, 'Rater')]
    role = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    email = forms.EmailField(max_length=254)

    def clean(self):
        cleaned_data = super(UpdateForm, self).clean()
        description = cleaned_data.get('description')
        role = cleaned_data.get('role')
        email = cleaned_data.get('email')

        if not role and not email and not description:
            raise forms.ValidationError('Please fill all fields.')


class FundsForm(forms.Form):
    addfunds = forms.IntegerField(required=True, label='Amount (€)')

    class Meta:
        model = User
        fields = ('addfunds')
