from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.decorators import login_required
from .models import User 

# Create your views here.

def registration(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        profile_pic = request.POST['profile_pic']
        password = request.POST['password']

        # check if user email is unique
        if User.objects.filter(email=email).exists():
            return redirect('registration')
        else:
            user = User.objects.create_user(
                password=password, email=email, profile_image=profile_pic,
                first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')
    else: 
        return render(request, 'user/register.html')
    

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect('top_page')
        else:
            return redirect('login')
    else:
        return render(request, "user/login.html")

def logout(request):
    auth.logout(request)
    return redirect('top_page')