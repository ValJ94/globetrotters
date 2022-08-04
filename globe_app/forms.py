from pyexpat import model
from select import select
from django import forms
from globe_app.models import *
from django.forms import ChoiceField, ModelForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'surname', 'age', 'description','picture', 'gender')

        first_name = forms.CharField(required=True)
        surname = forms.CharField(required=True)
        age = forms.IntegerField(required=True)
        gender = forms.CharField(required=True)

class upcomingTravelForm(ModelForm):
    class Meta:
        model = UpcomingTravel
        fields = ('dateStart', 'dateEnd', 'budgetStart', 'budgetEnd', 'dateFlexibility',)

        dateFlexibility = forms.TypedChoiceField(initial='Yes')

        
        labels = {
            'dateStart': '', 
            'dateEnd': '',
            'budgetStart': '',
            'budgetEnd': '',
            'dateFlexibility': 'Are the dates flexible?',
        }

        widgets = {
            'dateStart': forms.DateInput(attrs={'class':'form-control, col-xs-2', 
                                                'placeholder': 'Start date of trip', 
                                                'id': 'date_start'}), # form-control is bootstrap
            'dateEnd': forms.DateInput(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'End date of trip', 
                                                'id': 'date_end'}),
            'budgetStart': forms.NumberInput(attrs={'class':'form-control, col-xs-4', 
                                                    'placeholder': 'Budget from (in GBP): ',
                                                    'id': 'budget_start'}),
            'budgetEnd': forms.NumberInput(attrs={'class':'form-control, col-xs-6', 
                                                    'placeholder': 'Budget to (in GBP): ',
                                                    'id': 'budget_end'}),
        }


class MessageThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content', )
        
        labels = {
            'content': '', 
        }

        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control, col-xs-2', 
                                                'placeholder': 'Write here',}), 
        }