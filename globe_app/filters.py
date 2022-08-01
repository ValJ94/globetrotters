import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, ModelChoiceFilter

from .models import *
from django.contrib.auth.models import User


class BuddyFilter(django_filters.FilterSet):
    destination = ModelChoiceFilter(label="Current trip destinations", queryset=Destination.objects.all())
    dateStart = DateFilter(label="Date starting from or later than", lookup_expr='lte')
    dateEnd = DateFilter(label="Date until or earlier than", lookup_expr='gte')
    budgetStart = NumberFilter(label="Budget lower range (per day)", lookup_expr='lte')
    budgetEnd = NumberFilter(label="Budget higher range (per day)", lookup_expr='gte')
    # gender = ModelChoiceFilter(label="Gender", queryset=UserProfile.objects.values_list('gender', flat=True))
    # age = ModelChoiceFilter(label="Age", queryset=UserProfile.objects.values_list('age', flat=True))

    class Meta:
        model = UpcomingTravel
        fields = ('destination', 'dateStart', 'dateEnd', 'budgetStart', 'budgetEnd')
        # fields = ('destination', 'dateStart', 'dateEnd', 'budgetStart', 'budgetEnd','gender', 'age')


class UserFilter(django_filters.FilterSet):
    pass
    # class Meta:
    #     model = UserProfile
    #     fields = ('gender', 'age')


# class UsernameFilter(django_filters.FilterSet):

#     class Meta:
#         model = User
#         fields = ('user')