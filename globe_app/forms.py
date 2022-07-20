from pyexpat import model
from django import forms
from globe_app.models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'surname', 'age', 'description','picture')


# class upcomingTravelForm(forms.ModelForm):
#     class Meta:
#         model = UpcomingTravel
#         fields = ('destination', 'travelPics', 'travelNotes')