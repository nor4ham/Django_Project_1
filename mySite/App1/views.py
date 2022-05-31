from django.shortcuts import render,redirect,resolve_url
 # Create your views here.
from .models import Signup

def home(requset):
    return render(requset,'pages/home.html')
def about(requset):
   # x={'name':'nourah','age':'22'}
    return render(requset,'pages/about.html')
def signup(requset):
    if requset.method ==  'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')
        data=Signup(username = username,password =password )
        data.save()
    return render(requset,'pages/signup.html')
def login(requset):
    try:
     if requset.method ==  'POST':
        username=requset.POST.get('username')
        password=requset.POST.get('password')
        data=Signup.objects.get(username=username,password=password)
        return redirect(resolve_url("home"))
    except Exception as ve:
     print(ve.__class__)     
         
    return render(requset,'pages/login.html')
