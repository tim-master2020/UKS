from django.shortcuts import render
from .forms import UserForm, UserUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse


def editUser(request):
    if request.method == "POST":
        obj = request.user
        form = UserUpdateForm(request.POST or None, instance = obj)
        if form.is_valid(): 
            form.save()
            return redirect('/profile')
        else:
            print('not valid form when updating!',form.errors)
            return redirect('/profile')