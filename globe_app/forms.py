from django import forms
from globe_app.models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'middle_name', 'surname', 'age', 'description','picture')


