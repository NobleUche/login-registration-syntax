from email import message_from_string
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
       if request.method == 'POST':
              username=request.POST['username']
              email=request.POST['email']
              password=request.POST['password']
              password2=request.POST['password2']
              
              if password==password2:
                     if User.objects.filter(email=email).exists():
                            messages.info(request,'Email In Use')
                            return redirect('register')
                     elif User.objects.filter(username=username).exists():
                            messages.info(request,'Email In Use')
                            return redirect('register')
                     else:
                            user=User.objects.create_user(username=username, email=email, password=password)
                            user.save();
                            return redirect('login')
              else:
                     messages.info(request,'Password Not Same')
                     return redirect('register')
       else:
              return render(request,'register.html')


def login(request):
       if request.method=='POST':
              username=request.POST['username']
              password=request.POST['password']
              User = authenticate(username=username, password=password)
              if User is not None:
                     authenticate(request, User)
                     return redirect('/')
              else:
                     messages.info(request,'Wrong Credentials')
                     return redirect('login')
       else:
              return render(request,'login.html')              


          
                     
  
      


