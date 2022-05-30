from django.shortcuts import render,redirect
 # Create your views here.
from .models import Signup

def home(requset):
    return render(requset,'pages/home.html')
def about(requset):
   # x={'name':'nourah','age':'22'}
    return render(requset,'pages/about.html')
def login(requset):
    return render(requset,'pages/login.html')
def signup(requset):
    if requset.method ==  'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')
        data=Signup(username = username,password =password )
        data.save()
    return render(requset,'pages/signup.html')
def login(requset):
    if requset.method ==  'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')
        print("hoo",Signup.objects.get(username=username,password=password))
    return render(requset,'pages/login.html')
