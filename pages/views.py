from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from uuid import uuid4

# Create your views here.
def Index(request):
    return render(request, "index.html")


@csrf_exempt
def SignUp(request):
    if request.method == "POST":
        form = request.POST
        unique_id = uuid4()

        try:
            newUser = CustomUser.objects.create(username=unique_id, first_name=form['FirstName'], last_name=form['LastName'], phone_number=form['PhoneNumber'], password=make_password(f"{form['Password']}"), email=f"{form['Email']}", is_staff=False, is_superuser=False)
            user = authenticate(request, username=unique_id, password=form['Password'])
            login(request, user)
            return redirect('home')
        except:
            return HttpResponse("<h1>This is user already signup.<br><a href='/login/'>You can signIn.</h1><a href=''>Return Register page</a>")

    return render(request, "register.html")


@csrf_exempt
def SignIn(request):
    if request.method == "POST":
        form = request.POST
        username = form["UserName"]
        password = form["Password"]
        
        user = authenticate(request, first_name=username, password=password)
        
        if user is None:
            user = authenticate(request, email=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username yoki parol xato'})

    
    return render(request, "login.html")


def Logout(request):
    logout(request)
    return redirect('login')


def ResetPassword(request):
    return render(request, 'resetPassword.html')
