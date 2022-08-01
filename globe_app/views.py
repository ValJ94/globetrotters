from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Message, UserProfile, UpcomingTravel, Destination, MessageThread
from .forms import MessageThreadForm, ProfileForm, upcomingTravelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .filters import BuddyFilter, UserFilter
from django.views import View

from django.http import JsonResponse


def index(request):
    return render(request, 'globe_templates/index.html')

# Registration with customised fields (i.e., not supplied by Django Registration Redux Package)
# Code adapted from Tango With Django 2 (Azzopardi & Maxell, 2020)
@login_required
def register_contd(request):
    profile_form = ProfileForm()

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            user_profile = profile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('index'))
        else:
            print(profile_form.errors)

    context_dict = {'form': profile_form}
    return render(request, 'globe_templates/register_contd.html', context_dict)


# View profile
# Code adapted from the Tango With Django 2 book (Azzopardi & Maxell, 2020)
def profile(request, username):
    curr_user = User.objects.get(username=username)

    user_profile = UserProfile.objects.get_or_create(user=curr_user)[0]
    form = ProfileForm({'first_name': user_profile.first_name,
                        'middle_name': user_profile.middle_name,
                        'surname': user_profile.surname,
                        'age': user_profile.age,
                        'description': user_profile.description}) 

    context_dict = {'user_profile': user_profile,
                    'user': curr_user,
                    'form': form}

    return render(request,  'globe_templates/user_profile.html', context_dict)


def forum(request):
    context_dict = {}
    return render(request, 'globe_templates/forum.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'globe_templates/about.html', context_dict)

def upcoming_travels(request, owner):
    upcoming_data = UpcomingTravel.objects.filter(owner=owner)
    # upcoming_data = UpcomingTravel.objects.all()
    # print(UpcomingTravel.objects.all())
    context_dict = {'upcomingList': upcoming_data}

    return render(request, 'globe_templates/upcoming_travels.html', context_dict)

def travel_history(request):
    context_dict = {}
    return render(request, 'globe_templates/travel_history.html', context_dict)

def travel_wishlist(request):
    context_dict = {}
    return render(request, 'globe_templates/travel_wishlist.html', context_dict)

def travel_notes(request):
    context_dict = {}
    return render(request, 'globe_templates/travel_notes.html', context_dict)

def my_trips(request):
    context_dict = {}
    return render(request, 'globe_templates/my_trips.html', context_dict)

# add location template
# def add_location(request):
def add_upcoming_travel(request):
    upcoming_form = upcomingTravelForm()
    
    if request.method == 'POST':
        upcoming_form = upcomingTravelForm(request.POST)

        if upcoming_form.is_valid():
            upcoming_form.save(commit=True)
            return redirect(f'/globetrotters/upcoming_travels/{request.POST["owner"]}')
            # return render(request, 'globe_templates/upcoming_travels.html', context_dict)
        else:
            print(upcoming_form.errors)

    context_dict = {'form': upcoming_form,}

    return render(request, 'globe_templates/add_upcoming_travel.html', context_dict)


# save a location to the map
def save_location(request):
    destinationObject, created = Destination.objects.get_or_create(
        locationName = request.POST['locationFullName']
    )

# in case of adding new fields, you don't want to have copies of the same data
    if created:
        destinationObject.latitude = request.POST['latitude']
        destinationObject.longitude = request.POST['longitude']
        destinationObject.save()
    else:
        pass

    locationObject, created = UpcomingTravel.objects.get_or_create(
        destination = destinationObject,
        dateStart = request.POST['dateStart'],
        dateEnd = request.POST['dateEnd'],
        budgetStart = request.POST['budgetStart'],
        budgetEnd = request.POST['budgetEnd'],
        owner = request.POST['owner'],
    )


    return JsonResponse({'message':'Location saved'})
    # return redirect(f'/globetrotters/upcoming_travels/{request.POST["owner"]}')


# get the coordinates to show the locations on the map
def get_user_saved_locations(request, user):
    # owner = request.POST['user']
    print('Getting the locations now')

    # locationObjects = Destination.objects.all()
    locationObjects = UpcomingTravel.objects.filter(owner=user)

    lngLatList = [(record.destination.longitude, record.destination.latitude) for record in locationObjects]
    print(lngLatList)
    # lngLatList = [(record.longitude, record.latitude) for record in locationObjects]

    # The below coordinates will be retrieved by the user's saved locations model
    return JsonResponse({'locationList': lngLatList})


def find_buddy(request):
    myFilter = BuddyFilter(request.GET, queryset=UpcomingTravel.objects.all())
    myUserFilter = UserFilter(request.GET, queryset=UserProfile.objects.all())
    # myUsernameFilter = UsernameFilter(request.GET, queryset=User.objects.all())



    trips = myFilter.qs
    # tripsList = [trip.owner for trip in trips]
    # users = [User.objects.get(username=user) for user in tripsList]
    # print(users)
    users = myUserFilter.qs
    # usernames = myUsernameFilter.qs

    # owner = (User.username == UpcomingTravel.owner)


    context_dict = {'myFilter': myFilter, 'myUserFilter': myUserFilter, 
                    'trips': trips, 'users': users, }
    # context_dict = {'myFilter': myFilter, 'myUserFilter': myUserFilter, 'myUsernameFilter': myUsernameFilter, 
    #                 'trips': trips, 'users': users, 'usernames': usernames}

    return render(request, 'globe_templates/find_buddy.html', context_dict)


def buddy_search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        destinations = UpcomingTravel.objects.filter(destination__locationName__icontains=searched)
        return render(request, 
        'globe_templates/buddy_search_results.html', 
        {'searched': searched,
        'destinations': destinations})
    else:
        return render(request, 'globe_templates/buddy_search_results.html')

# Messaging
class ListThreads(View):
    def get(self, request, *args, **kwargs):
        messageThreads = MessageThread.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context_dict = {'messageThreads': messageThreads}

        return render(request, 'globe_templates/inbox.html', context_dict)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = MessageThreadForm()
        context_dict = {'form': form}

        return render(request, 'globe_templates/create_message_thread.html', context_dict)

    def post(self, request, *args, **kwargs):
        form = MessageThreadForm()

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if MessageThread.objects.filter(user=request.user, receiver=receiver).exists(): 
                messageThread = MessageThread.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=messageThread.pk)
            elif MessageThread.objects.filter(user=receiver, receiver=request.user).exists():
                messageThread = MessageThread.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=messageThread.pk)
            
            if form.is_valid():
                messageThread = MessageThread(user=request.user, receiver=receiver)
                messageThread.save()
                return redirect('thread', pk=messageThread.pk)
        # if the user doesn't exist:
        except:
            return redirect('create_message_thread')

