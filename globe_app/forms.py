from pyexpat import model
from django import forms
from globe_app.models import *
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'surname', 'age', 'description','picture', 'gender')


class upcomingTravelForm(ModelForm):
    class Meta:
        model = UpcomingTravel
        fields = ('destination', 'dateStart', 'dateEnd', 'budgetStart', 'budgetEnd')

        labels = {
            'destination': 'Destination',
            'dateStart': '', 
            'dateEnd': '',
            'budgetStart': '',
            'budgetEnd': '',
        }

        widgets = {
            'dateStart': forms.DateInput(attrs={'class':'form-control, col-xs-2', 
                                                'placeholder': 'Start date of trip', 
                                                'id': 'date_start'}), # form-control is bootstrap
            'dateEnd': forms.DateInput(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'End date of trip', 
                                                'id': 'date_end'}),
            'budgetStart': forms.NumberInput(attrs={'class':'form-control, col-xs-4', 
                                                    'placeholder': 'Budget from (in GBP): '}),
            'budgetEnd': forms.NumberInput(attrs={'class':'form-control, col-xs-6', 
                                                    'placeholder': 'Budget to (in GBP): '}),
        }