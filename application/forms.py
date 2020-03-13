from django.forms import ModelForm
from application.models import Application
from django import forms

class JobForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        # exclude = ['age']
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['other_name'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'eg: 03/27/2020'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = '+256784756467'
        self.fields['email_address'].widget.attrs['class'] = 'form-control'
        self.fields['email_address'].widget.attrs['placeholder'] = 'myname@example.com'
        self.fields['educ_background'].widget.attrs['class'] = 'form-control'
        self.fields['educ_background'].widget.attrs['rows'] = '6'
        self.fields['training'].widget.attrs['class'] = 'form-control'
        self.fields['training'].widget.attrs['rows'] = '6'
        self.fields['experience'].widget.attrs['class'] = 'form-control'
        self.fields['experience'].widget.attrs['rows'] = '6'
        self.fields['publication'].widget.attrs['class'] = 'form-control'
        self.fields['publication'].widget.attrs['rows'] = '6'
        self.fields['publication'].widget.attrs['placeholder'] = 'A must Field For for Positions that Require Publication'
        self.fields['position'].widget = forms.HiddenInput()
        self.fields['age'].widget = forms.HiddenInput()