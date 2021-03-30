from django.contrib import auth
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def sign_up(request):
    if request.POST:
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username,email,password)

        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        return redirect('home')
    else:
        return render(request,"myapp/registration.html")

def sign_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        print("----> inside the login",user)

        if user is not None:
            login(request,user)
            print("---------------->",user)
            messages.success(request,"successfully logged in")
            print("=====> login ")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials ")
            return redirect('home')
    else:
        return render(request,"myapp/login.html")   

def user_logout(request):
    logout(request)
    return redirect('home')

