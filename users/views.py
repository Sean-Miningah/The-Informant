from django.shortcuts import render
from django.contrib import messages, auth 
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from .models import User 

# Create your views here.

def registration(request):
    if request.method == 'POST':
        # Get form values
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
        # email = request.POST['email']
        # profile_pic = request.POST['profile_pic']
        # password = request.POST['password']
        # password2 = request.POST['password2']

        # print(username)
        return render(request, 'user/register.html')

        # # check if password match
        # if password == password2: 
        #     print('success')
        #     if User.objects.filter(username=username).exists():
        #         messages.error(request, 'That username is taken')
        #         return redirect('register')
        #     else:
        #         if User.objects.filter(email=email).exists():
        #             messages.error(request, 'Email is already registered')
        #             return redirect('register')
        #         else:
        #             user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        #             # Login after register
        #             # auth.login(request, user)
        #             # messages.success(request, 'You are now logged in')
        #             # return redirect('index')
        #             user.save()
        #             messages.success(request, 'You are now registered')
        #             return redirect('login')
        # else: 
        #     messages.error(request, 'Passwords do not match')
        #     return redirect('register')
    else:
        # return render(request, 'user/register.html')
        return render(request, 'user/register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return render(request, 'accounts/login.html')
#     else:
#         return render(request, 'accounts/login.html')       

def login(request):
    if request.method == "POST":
        return render(request, "user/login.html")
    else:
        return render(request, "user/login.html")