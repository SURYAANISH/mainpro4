from django.contrib import messages
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.shortcuts import render,redirect
from .models import Dress

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    content=Dress.objects.all()
    data={
        'result':content
    }
    return render(request,'home.html',data)

def card1(request):
    content=Dress.objects.all()
    data={
        'result':content
    }
    return render(request,'card1.html',data)


def card2(request):
    content=Dress.objects.all()
    data={
        'result':content
    }
    return render(request,'card2.html',data)

def card3(request):
    content=Dress.objects.all()
    data={
        'result':content
    }
    return render(request,'card3.html',data)

def details(request,id):
    product=Dress.objects.get(pk=id)
    print(product)
    data={
        'data':product
    }
    return render(request,'details.html',data)
# USER AUTHENTICATION PART
def signup(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('pass')
            password2=request.POST.get('cpass')
            if password1==password2:
                if User.objects.filter(username=username,email=email).exists():
                    messages.info(request,'username already exists!!!!')
                    print("already have")
                else:
                    new_user=User.objects.create_user(username,email,password1)
                    new_user.save()
                    return redirect(user_login)
            else:
                print('wrong password')
        return render(request,'signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password1=request.POST.get('pass1')
            user=authenticate(request,username=username,password=password1)
            if user is not None:
                login(request,user)
                return redirect(home)
            else:
                messages.info(request,'user not exists')
                print('user no exist')

        return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(home)

def details(request,id):
    product=Dress.objects.get(pk=id)
    print(product)
    data={
        'data':product
    }
    return render(request,'details.html',data)
