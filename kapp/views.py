from django.shortcuts import render, redirect
from django.http import HttpResponse
from kapp.models import SignUp, Contact

# Import necessary modules and models
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *



def index(request):
    return render(request,"kapp/index.html")
def help(request):
    return render(request,"kapp/help.html")

def signUp(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        e_mail=request.POST['e_mail']
        password=request.POST['password']
        if len(first_name) < 2 or len(last_name) < 2 or len(e_mail) < 5 or len(password) < 2:
            return redirect('index')
        else:
            save_data= SignUp(first_name=first_name, last_name=last_name, e_mail=e_mail, password=password)
            save_data.save()
            return redirect('signup')   
    return render(request, 'kapp/signup.html')


def contactUs(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        e_mail=request.POST['e_mail']
        phone_number=request.POST['phone_number']
        contact_message=request.POST['contact_message']
        if len(first_name) < 2 or len(last_name) < 2 or len(e_mail) < 5 or len(phone_number) < 9 or len(contact_message) < 5:
            return redirect('index')
        else:
            save_data= Contact(first_name=first_name, last_name=last_name, e_mail=e_mail, phone_number=phone_number, contact_message=contact_message)
            save_data.save()
            return redirect('contact_us')   
    return render(request, 'kapp/contact_us.html')

def login(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/index/')
     
    # Render the login page template (GET request)
    return render(request, 'kapp/login.html')

# username:sumaida@rampure
# pass:sumaida@123