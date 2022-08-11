from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Message, TravelHistory, TravelWishlist, UserProfile, UpcomingTravel, Destination, MessageThread
from .forms import MessageForm, MessageThreadForm, ProfileForm, upcomingTravelForm, MessageForm, TravelHistoryForm, TravelWishlistForm
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


def about(request):
    context_dict = {}
    return render(request, 'globe_templates/about.html', context_dict)


# UPCOMING TRAVELS

def upcoming_travels(request, owner):
    upcoming_data = UpcomingTravel.objects.filter(owner=owner)
    # upcoming_data = UpcomingTravel.objects.all()
    # print(UpcomingTravel.objects.all())
    context_dict = {'upcomingList': upcoming_data}

    return render(request, 'globe_templates/upcoming_travels.html', context_dict)

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

    # if locationObject:
    locationObject, created = UpcomingTravel.objects.get_or_create(
        destination = destinationObject,
        dateStart = request.POST['dateStart'],
        dateEnd = request.POST['dateEnd'],
        budgetStart = request.POST['budgetStart'],
        budgetEnd = request.POST['budgetEnd'],
        owner = request.POST['owner'],
        travelNotes = request.POST['noteContent'],
        )

    return JsonResponse({'message':'Location saved'})
    # return redirect(f'/globetrotters/upcoming_travels/{request.POST["owner"]}')


# get the coordinates to show the locations on the maps
def get_user_saved_locations(request, user):
    # owner = request.POST['user']
    print('Getting the locations now')

    # locationObjects = Destination.objects.all()
    locationObjects = UpcomingTravel.objects.filter(owner=user) # for upcoming travels

    lngLatList = [(record.destination.longitude, record.destination.latitude) for record in locationObjects]
    print(lngLatList)
    # lngLatList = [(record.longitude, record.latitude) for record in locationObjects]

    # The below coordinates will be retrieved by the user's saved locations model
    return JsonResponse({'locationList': lngLatList})



# TRAVEL HISTORY

def travel_history(request, owner):
    history_data = TravelHistory.objects.filter(owner=owner)

    context_dict = {'historyList': history_data}
    return render(request, 'globe_templates/travel_history.html', context_dict)


def add_history(request):
    history_form = TravelHistoryForm()
    
    if request.method == 'POST':
        history_form = TravelHistoryForm(request.POST, request.FILES)

        if history_form.is_valid():
            history_form.save(commit=True)
            return redirect(f'/globetrotters/travel_history/{request.POST["owner"]}')
            # return render(request, 'globe_templates/upcoming_travels.html', context_dict)
        else:
            print(history_form.errors)

    context_dict = {'form': history_form,}

    return render(request, 'globe_templates/add_history.html', context_dict)

# save a location to the map
def save_history_location(request):
    print(request.POST)
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

    # if locationObject:
    historyLocationObject, created = TravelHistory.objects.get_or_create(
        destination = destinationObject,
        owner = request.POST['owner'],
        travelPics = request.POST['travelPics'],
        travelNotes = request.POST['noteContent'],
    )

    return JsonResponse({'message':'Location saved'})

def get_user_saved_history_locations(request, user):
    print('Getting the locations now')

    historyLocationObject = TravelHistory.objects.filter(owner=user) # for upcoming travels

    lngLatList = [(record.destination.longitude, record.destination.latitude) for record in historyLocationObject]
    print(lngLatList)

    return JsonResponse({'locationHistoryList': lngLatList})



# TRAVEL WISHLIST

def travel_wishlist(request, owner):
    wishlist_data = TravelWishlist.objects.filter(owner=owner)

    context_dict = {'wishlistList': wishlist_data}
    return render(request, 'globe_templates/travel_wishlist.html', context_dict)


def add_wishlist(request):
    wishlist_form = TravelWishlistForm()
    
    if request.method == 'POST':
        wishlist_form = TravelWishlistForm(request.POST)

        if wishlist_form.is_valid():
            wishlist_form.save(commit=True)
            return redirect(f'/globetrotters/travel_wishlist/{request.POST["owner"]}')
            # return render(request, 'globe_templates/upcoming_travels.html', context_dict)
        else:
            print(wishlist_form.errors)

    context_dict = {'form': wishlist_form,}

    return render(request, 'globe_templates/add_wishlist.html', context_dict)

# save a location to the map
def save_wishlist_location(request):
    print(request.POST)
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

    # if locationObject:
    wishlistLocationObject, created = TravelWishlist.objects.get_or_create(
        destination = destinationObject,
        owner = request.POST['owner'],
        travelNotes = request.POST['noteContent'],
    )

    return JsonResponse({'message':'Location saved'})

def get_user_saved_wishlist_locations(request, user):
    print('Getting the locations now')

    wishlistLocationObject = TravelWishlist.objects.filter(owner=user) # for upcoming travels

    lngLatList = [(record.destination.longitude, record.destination.latitude) for record in wishlistLocationObject]
    print(lngLatList)

    return JsonResponse({'locationWishlistList': lngLatList})




def travel_notes(request):
    context_dict = {}
    return render(request, 'globe_templates/travel_notes.html', context_dict)

def my_trips(request):
    context_dict = {}
    return render(request, 'globe_templates/my_trips.html', context_dict)



def find_buddy(request):
    myBuddyFilter = BuddyFilter(request.GET, queryset=UpcomingTravel.objects.all().order_by('-destination'))
    myUserFilter = UserFilter(request.GET, queryset=UserProfile.objects.all())

    trips = myBuddyFilter.qs.order_by('-destination')
    users = myUserFilter.qs

    context_dict = {'myFilter': myBuddyFilter, 'myUserFilter': myUserFilter, 
                    'trips': trips, 'users': users, }
    return render(request, 'globe_templates/find_buddy.html', context_dict)


def search_users(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # destinations = UpcomingTravel.objects.filter(destination__locationName__icontains=searched)
        users = UserProfile.objects.filter(user__username__icontains=searched)
        return render(request, 
        'globe_templates/search_users.html', 
        {'searched': searched,
        'users': users,})
        # 'destinations': destinations})
    else:
        return render(request, 'globe_templates/search_users.html')



# Messaging
# Code adapted from Legion Script on Youtube (https://www.youtube.com/watch?v=oxrQdZ5KqW0) (see bibliography)
def list_threads(request):
    threads = MessageThread.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    
    threadList = []
    for thread in threads:
        threadMessages = Message.objects.filter(messageThread=thread)
        unreadThreadMessages = Message.objects.filter(messageThread=thread, messageRead=False, messageReceiver=thread.user)
        threadList.append({
            "thread": thread,
            "messages": {
                # "totalMessages": len(threadMessages), # here for testing 
                "unreadMessages": len(unreadThreadMessages)
            }
        })

    context_dict = {'threadList': threadList}

    return render(request, 'globe_templates/inbox.html', context_dict)



def thread_view(request, pk):
    print(pk)
    form = MessageForm()
    thread = MessageThread.objects.get(pk=pk) # the thread we'll show on screen
    messageList = Message.objects.filter(messageThread__pk__contains=pk)

    print(pk)
    print(thread.user.username)

    # Get the messages from the messageList that belong to the TO user who's requesting them
    # Check whichever are unread and change their status to True (Since after you retrieve them the user has read them)
    # messageToList = [message for message in messageList if message.messageReceiver == thread.user]
    
    messageToList = []
    for message in messageList:
        if message.messageReceiver == thread.user:
            messageToList.append(message)

    for message in messageToList:
        if not message.messageRead:
            message.messageRead = True
            message.save()

    context_dict = {'thread': thread, 'form': form, 'messageList': messageList}

    return render(request, 'globe_templates/message_thread.html', context_dict)


def create_message(request, pk):
    # Just one POST method
    thread = MessageThread.objects.get(pk=pk)

    # Make sure we have the right user
    if thread.receiver == request.user:
        receiver = thread.user
    else:
        receiver = thread.receiver
    
    content = Message(messageThread = thread, 
                    messageSender=request.user,
                    messageReceiver=receiver,
                    content=request.POST.get('content'))
    
    content.save()
    return redirect('globe_app:thread', pk=pk)


def create_or_find_message_thread(request, username, receiver):
    
    print(username)
    print(receiver)

    senderObject = User.objects.get(username=username)
    try:
        receiverObject = User.objects.get(username=receiver)
    except Exception as e:
        print('User probably doesnt exist')
        return redirect(f'/globetrotters/find_buddy/')

    messageThread = MessageThread.objects.get_or_create(user=senderObject, receiver=receiverObject)
    print(messageThread)
    # (<MessageThread: MessageThread object (5)>, False)
    return redirect(f'/globetrotters/inbox/{messageThread[0].pk}/')
