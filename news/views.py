from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Story



# Create your views here.
def index(request):
    stories = Story.objects.all().order_by('-Datetime')
    # nation_stories = Story.objects.order_by('-Datetime').filter(
    #     source ="Nation Media").exclude(img_url=None)[:4]
    pd_stories = Story.objects.filter(
        source="People Daily").order_by('-Datetime')[:4]

    context = {
        pd_stories : 'pd_stories',
    }
    # print(type(pd_stories))
    # print(dir(pd_stories))
    # print(dir(stories))
    print(pd_stories)
    # for story in stories:
    #     print(story)
    # return HttpResponse('<h1>Page Found</h1>')
<<<<<<< HEAD
    return render(request, 'index.html', context)


def comments(request):

    return render(request, "comments.html")
=======
    return render(request, 'index.html')
>>>>>>> parent of dd2df6f... comments model registered in dashboard
