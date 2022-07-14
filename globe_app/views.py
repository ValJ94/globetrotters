from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from globe_app.models import UserProfile
from globe_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.utils.decorators import method_decorator
from django.views import View


def index(request):
    return render(request, 'globe_templates/index.html')

# Registration with customised fields (i.e., not supplied by Django Registration Redux Package)
@login_required
def register_contd(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'globe_templates/register_contd.html', context_dict)



class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist: 
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = ProfileForm({'first_name': user_profile.first_name,
                            'middle_name': user_profile.middle_name,
                            'surname': user_profile.surname,
                            'age': user_profile.age,
                            'description': user_profile.description}) 
        
        return (user, user_profile, form)
    
    @method_decorator(login_required) 
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'globe_templates/user_profile.html', context_dict)



def profile(request, username):

    # return HttpResponse('hello')

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

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES, instance=user_profile)

    #     if form.is_valid():
    #         form.save(commit=True)
    #         return redirect('user_profile', user.name)
        
    #     return render(request, 'globe_templates/user_profile.html', context_dict)
        
    # elif request.method == 'GET':
    return render(request,  'globe_templates/user_profile.html', context_dict)



