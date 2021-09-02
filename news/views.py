from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Story
from users.models import Comments



# Create your views here.
def index(request):
    stories = Story.objects.all().order_by('-Datetime')
    nation_stories = Story.objects.order_by('-Datetime').filter(
        source ="Nation Media").exclude(img_url=None)[:4]
    # pd_stories = Story.objects.filter(
    #     source="People Daily").order_by('-Datetime')[:4]
    # pd_images = pd_stories.img_url
    # pd_titles = pd_stories.title
    # nation_stories = Story.objects.filter(source="Nation Media").order_by('-Datetime')[:4]
    # nation_images = nation_stories.img_url 
    # nation_titles = nation_storis.title

    context = {
        nation_stories : 'nation_stories',
    }
    # print(type(pd_stories))
    # print(dir(pd_stories))
    # print(dir(stories))
    print(nation_stories)
    # for story in stories:
    #     print(story)
    # return HttpResponse('<h1>Page Found</h1>')
    return render(request, 'index.html', context)


def comments(request):

    return render(request, "comments.html")
