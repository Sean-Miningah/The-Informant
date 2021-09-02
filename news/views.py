from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Story
from users.models import Comments


# Create your views here.
def index(request):

    # return HttpResponse('<h1>Page Found</h1>')
    return render(request, 'index.html')


def comments(request):

    return render(request, "comments.html")
