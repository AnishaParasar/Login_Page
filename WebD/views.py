from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    messages.success(request, "Home page")
    return render(request, "WebD/index.html")

@csrf_exempt
def signup(request):
    # print("In sign Up")
    if request.method == "POST":
        print("In post method")
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(username)
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.middle_name = mname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect("signin")
    return render(request, "WebD/signup.html")

@csrf_exempt
def signin(request):
    print("In Sign In")
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "WebD/index.html", {'fname': fname})
        else:
            return redirect('home')

    return render(request, "WebD/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

