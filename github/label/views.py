from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Label

# Create your views here.

def all(request):
    labels = Label.objects.all
    context = {'all_labels': labels}
    return render(request, 'label/all-labels.html',context)