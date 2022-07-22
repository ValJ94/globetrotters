from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from globe_app.models import *
from globe_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

def find_buddy(request):
    context_dict = {}
    return render(request, 'globe_templates/find_buddy.html', context_dict)

def upcoming_travels(request):
        
    print('show upcoming working')
    upcoming_data = UpcomingTravel.objects.all()
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
            return redirect('/globetrotters/upcoming_travels/')
        else:
            print(upcoming_form.errors)

    context_dict = {'form': upcoming_form}
    return render(request, 'globe_templates/add_upcoming_travel.html', context_dict)


# save a location to the map
def save_location(request):
    # print(request.POST['longitude'])
    # print(request.POST['latitude'])
    # print(request.POST['locationFullName'])

    locationObject, created = Destination.objects.get_or_create(
        locationName = request.POST['locationFullName']
    )

# in case of adding new fields, you don't want to have copies of the same data
    if created:
        locationObject.latitude = request.POST['latitude']
        locationObject.longitude = request.POST['longitude']
        locationObject.save()
    else:
        pass

    return JsonResponse({'message':'Location saved'})

# def add_upcoming_details(request):
#     # form for other fields in upcoming travels
#     upcoming_travel_form = upcomingTravelForm()
    
#     if request.method == 'POST':
#         upcoming_travel_form = upcomingTravelForm(request.POST)

#         if upcoming_travel_form.is_valid():
#             # save the travel details to the db
#             upcoming_travel_form.save(commit=True)
#             # redirect user back to the index view
#             return redirect('/index/')
#         else:
#             print(upcoming_travel_form.errors)

#     return render(request,  'globe_templates/add_location.html', {'form': upcoming_travel_form})



# get the coordinates to show the locations on the map
def get_user_saved_locations(request):
    print('Getting the locations now')

    locationObjects = Destination.objects.all()
    lngLatList = [(record.longitude, record.latitude) for record in locationObjects]
    # The below coordinates will be retrieved by the user's saved locations model
    return JsonResponse({'locationList': lngLatList})
