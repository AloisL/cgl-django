from django.contrib.auth.forms import UserCreationForm
from django import forms
from member.models import Member

class InscriptionForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	class Meta:
		model = Member
		fields = UserCreationForm.Meta.fields + ('email',)
