from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    size = forms.IntegerField(required=False)
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    cohortLocations = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.CohortLocations.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    cohortRules = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.CohortRules.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        cohort = models.Cohort.objects.get(pk=pk)
        photo.cohort = cohort 
        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Cohort 
        fields = (
            'name',
            'description',
            'city',
            'price',
            'guests',
            'size',
            'check_in',
            'check_out',
            'instant_book',
            'cohort_guide',
            'cohortName',
            'cohortLocations',
            'cohortRules',
        )

    def save(self, *args, **kwargs):
        cohort = super().save(commit=False)
        return cohort