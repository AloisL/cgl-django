from django import forms

class NewProject(forms.Form):
    title = forms.CharField(max_length = 200)
    donationGoal = forms.CharField()
    description = forms.CharField(
        max_length = 5000,
        widget = forms.Textarea(),
        help_text = 'Write here a description of your project (5000 caracters max.)')
    deadline = forms.DateField()

    def clean(self):
        cleaned_data = super(NewProject, self).clean()
        donationGoal = cleaned_data.get('donationGoal')
        description= cleaned_data.get('description')
        name = cleaned_data.get('name')
        if not name and not donationGoal and not description:
            raise forms.ValidationError('You have to fill all fields of the form!')

class NewComment(forms.Form):
    title = forms.CharField(max_length = 50)
    content = forms.CharField(widget=forms.Textarea, max_length = 500)

    def clean(self):
        cleaned_data = super(NewComment, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError('You have to fill all fields of the form!')