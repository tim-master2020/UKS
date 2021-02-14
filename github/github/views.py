from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from user.forms import UserForm, UserUpdateForm
from photo.forms import PhotoForm
from django.contrib.auth import authenticate
from django.contrib import messages
from photo.models import Photo
from repository.models import Repository
from django.contrib.auth.models import User

# Get questions and display them
def landing(request):
    if(request.user is not None):
        allRepositories = Repository.objects.filter(users=request.user.id)
        # branchCount = Branch.objects.all()

        allUsers = User.objects.exclude(username=request.user)
        context = {'allRepositories': allRepositories}
        return render(request, "landing/landing.html", context)
    
    return render(request, 'landing/landing.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            registered = True
            messages.success(request, 'Your account has been created! You are able to log in now!')
            return redirect('login')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def profile(request):
    user = request.user
    form = UserUpdateForm(instance = user) 
    photoForm = PhotoForm()
    image = None if not Photo.objects.filter(users_id = request.user.id) else Photo.objects.filter(users_id = request.user.id)[0]
    # image = Photo.objects.get(users_id = request.user.id)
    return render(request,'profile/profile.html',{'user_update_form':form, 'photo_form':photoForm, 'image':image})
