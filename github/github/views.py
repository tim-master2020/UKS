from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Get questions and display them
def landing(request):
    return render(request, 'landing/landing.html')