from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.shortcuts import render,redirect
from .models import Dress
from .forms import DressForm
# Create your views here.



def home(request):
    content=Dress.objects.all()
    data={
        'result':content
    }
    return render(request,'home.html',data)

