from django import forms

class NewProject(forms.Form):
    title = forms.CharField(max_length = 200)
    price = forms.CharField()
    short_description = forms.CharField(
        max_length = 500,
        widget = forms.Textarea(),
        help_text = 'Write here a short description of your project (500 caracters max.)')
    description = forms.CharField(
        widget = forms.Textarea(),
        help_text = 'Write here the description of your project.')
    deadline = forms.DateField()

    def clean(self):
        cleaned_data = super(NewProject, self).clean()
        name = cleaned_data.get('name')
        money_needed = cleaned_data.get('money_needed')
        short_description = cleaned_data.get('short_description')
        description= cleaned_data.get('description')
        if not name and not money_needed and not short_description and not description:
            raise forms.ValidationError('You have to fill all fields of the form!')

class NewComment(forms.Form):
    title = forms.CharField(max_length = 50)
    content = forms.CharField(widget=forms.Textarea, max_length = 200)

    def clean(self):
        cleaned_data = super(NewComment, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError('You have to fill all fields of the form!')