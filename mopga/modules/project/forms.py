from django import forms
from django.forms import SelectDateWidget

from mopga.modules.project.models import Projects


class NewProject(forms.Form):
    title = forms.CharField(max_length=200)
    donationGoal = forms.IntegerField(label='Donation goal', min_value=0)
    description = forms.CharField(max_length=5000, widget=forms.Textarea(),
                                  help_text='Write here a description of your project (5000 caracters)')
    # TODO: date > now()
    deadline = forms.DateField(widget=SelectDateWidget(empty_label=("Year", "Month", "Day"),
                                                       attrs=({
                                                           'style': 'width: 32%; display: inline-block; margin: 5px;'})))
    image = forms.ImageField(allow_empty_file=False)

    def clean(self):
        cleaned_data = super(NewProject, self).clean()
        donationGoal = cleaned_data.get('donationGoal')
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')
        image = cleaned_data.get('image')

        if not name and not donationGoal and not description and not image:
            raise forms.ValidationError('Please fill all fields.')


class AddNote(forms.Form):
    note = forms.IntegerField(min_value=0, max_value=5)

    def clean(self):
        cleaned_data = super(AddNote, self).clean()
        note = cleaned_data.get('note')
        if note < 0 or note > 5:
            raise forms.ValidationError('The note must be between 0 and 5')


class NewComment(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    content = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 2}), required=False)

    def clean(self):
        cleaned_data = super(NewComment, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError('Please fill all fields.')


class AddFundsProject(forms.Form):
    addfunds = forms.IntegerField(required=False, label='Funds Project ? (€)')

    class Meta:
        model = Projects
        fields = ('addfunds')
