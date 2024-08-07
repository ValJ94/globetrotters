from django import forms
from globe_app.models import TravelWishlist, UpcomingTravel, Message, TravelHistory, UserProfile
from django.forms import  ModelForm


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
        fields = ('dateStart', 'dateEnd', 'budgetStart', 'budgetEnd', 'travelNotes')

        dateFlexibility = forms.TypedChoiceField(initial='Yes')

        
        labels = {
            'dateStart': '', 
            'dateEnd': '',
            'budgetStart': '',
            'budgetEnd': '',
            'travelNotes': '',
            # 'dateFlexibility': 'Are the dates flexible?',
        }

        widgets = {
            'dateStart': forms.DateInput(attrs={'class':'form-control, col-xs-2', 
                                                'placeholder': 'Start date of trip', 
                                                'id': 'date_start',}), # form-control is bootstrap
            'dateEnd': forms.DateInput(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'End date of trip', 
                                                'id': 'date_end'}),
            'budgetStart': forms.NumberInput(attrs={'class':'form-control, col-xs-4', 
                                                    'placeholder': 'Daily budget from (in GBP): ',
                                                    'id': 'budget_start'}),
            'budgetEnd': forms.NumberInput(attrs={'class':'form-control, col-xs-6', 
                                                    'placeholder': 'Daily budget to (in GBP): ',
                                                    'id': 'budget_end'}),
            'travelNotes': forms.Textarea(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'Write some notes on the destination', 
                                                'id': 'travel_note'}),
        }


class TravelHistoryForm(ModelForm):
    class Meta:
        model = TravelHistory
        # fields = ('travelPics', 'travelNotes')
        fields = ('travelNotes',)

        labels = {
            # 'travelPics': '', 
            'travelNotes': '',
        }

        widgets = {
            # 'travelPics': forms.FileInput(attrs={'class':'form-control, col-xs-2', 
            #                                     'placeholder': 'Upload travel pictures', 
            #                                     'id': 'travel_pic',}), # form-control is bootstrap
            'travelNotes': forms.Textarea(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'Write some notes on the destination', 
                                                'id': 'travel_note'}),
        }


class TravelWishlistForm(ModelForm):
    class Meta:
        model = TravelWishlist
        fields = ('travelNotes',)

        labels = {
            'travelNotes': '',
        }

        widgets = {
            'travelNotes': forms.Textarea(attrs={'class':'form-control, col-xs-3', 
                                                'placeholder': 'Write some notes on the destination', 
                                                'id': 'travel_note'}),
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
            'content': forms.Textarea(attrs={'class':'form-control', 
                                                'placeholder': 'Write here',}), 
        }