from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def addPhoto(request): 
    print(request.user.id)
    if request.method == 'POST': 
        form = PhotoForm(request.POST, request.FILES) 
        
        if form.is_valid():
            photo = form.save(commit=False)
            currentUser = User.objects.get(id = request.user.id)
            photo.users = currentUser
            photo.save()
            return redirect('/profile')
    else: 
        form = PhotoForm() 
    return redirect('/profile') 
