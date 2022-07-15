from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from globe_app.models import UserProfile
from globe_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'globe_templates/index.html')

# Registration with customised fields (i.e., not supplied by Django Registration Redux Package)
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



