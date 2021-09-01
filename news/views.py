from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Story


# Create your views here.
def index(request):
    test = Story.objects.exclude(source="People Daily")[0]
    link = 'ok'

    # return HttpResponse('<h1>Page Found</h1>')
    return render(request, 'base.html', {'title': test.id, 'link': link})