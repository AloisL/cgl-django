from django import forms


class SearchProjectForm(forms.Form):
    title = forms.CharField(required=False)
    donationGoalMin = forms.IntegerField(min_value=0, required=False)
    donationGoalMax = forms.IntegerField(min_value=0, required=False)
    donationRateMin = forms.IntegerField(min_value=0, max_value=100, required=False)
    donationRateMax = forms.IntegerField(min_value=0, max_value=100, required=False)
    makerKarmaMin = forms.IntegerField(required=False)
    makerKarmaMax = forms.IntegerField(required=False)

    # TODO Filtrage par date

    def clean(self):
        cleaned_data = super(SearchProjectForm, self).clean()
        title = cleaned_data.get('title')
        donationGoalMin = cleaned_data.get('donationGoalMin')
        donationGoalMax = cleaned_data.get('donationGoalMax')
        donationRateMin = cleaned_data.get('donationRateMin')
        donationRateMax = cleaned_data.get('donationRateMax')
        makerKarmaMin = cleaned_data.get('makerKarmaMin')
        makerKarmaMax = cleaned_data.get('makerKarmaMax')

        if not title and not donationGoalMin and not donationGoalMax and not donationRateMin and not donationRateMax and not makerKarmaMin and not makerKarmaMax:
            raise forms.ValidationError('Please fill all fields.')

