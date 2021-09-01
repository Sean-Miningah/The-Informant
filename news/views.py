from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseNotFound 


# Create your views here.
def index(request):
    return HttpResponse('<h1>Page Found</h1>')