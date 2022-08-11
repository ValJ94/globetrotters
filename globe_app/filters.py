import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter, ModelChoiceFilter

from .models import UpcomingTravel, Destination


class BuddyFilter(django_filters.FilterSet):
    destination = ModelChoiceFilter(label="Current trip destinations", queryset=Destination.objects.all())
    dateStart = DateFilter(label="Date starting from or later than", lookup_expr='lte')
    dateEnd = DateFilter(label="Date until or earlier than", lookup_expr='gte')
    budgetStart = NumberFilter(label="Budget lower range (per day)", lookup_expr='lte')
    budgetEnd = NumberFilter(label="Budget higher range (per day)", lookup_expr='gte')

    class Meta:
        model = UpcomingTravel
        fields = ('destination', 'dateStart', 'dateEnd', 'budgetStart', 'budgetEnd')


class UserFilter(django_filters.FilterSet):
    pass
    # class Meta:
    #     model = UserProfile
    #     fields = ('gender', 'age')
