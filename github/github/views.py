from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from user.models import UserForm
from django.contrib.auth import authenticate
from django.contrib import messages

# Get questions and display them
def landing(request):
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

