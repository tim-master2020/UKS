from django.shortcuts import render
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect,
                              redirect)
from django.urls import reverse
from urllib.parse import urlencode
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Label
from .forms import LabelForm
from repository.models import Repository
from repository.views import detail_view
from django.core.exceptions import ValidationError

# Create your views here.

def all(request):
    labels = Label.objects.all
    context = {'all_labels': labels}
    return render(request, 'label/all-labels.html',context)