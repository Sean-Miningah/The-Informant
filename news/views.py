from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound 
from .models import Story
from users.models import User, Comments



# Create your views here.
def index(request):
    stories = Story.objects.all().order_by('-Datetime')
    # nation_stories = Story.objects.order_by('-Datetime').filter(
    #     source ="Nation Media").exclude(img_url=None)[:4]
    pd_stories = Story.objects.filter(
        source="People Daily").order_by('-Datetime')[:4]
    nation_stories = Story.objects.filter(
        source="Nation Media").exclude(img_url=None).order_by('-Datetime')[:4]
    
    sources = Story.objects.values_list('source').distinct()
    tags = Story.objects.values_list('category').distinct()
    latest_comments = Comments.objects.order_by('-date_created')[:9]
    latest_news = Story.objects.exclude(img_url=None).order_by('-Datetime')[:5]

    context = {
        'pd_stories' : pd_stories,
        'nation_stories' : nation_stories,
        'sources' : sources,
        'tags' : tags,
        'latest_comments' : latest_comments,
        'latest_news' : latest_news
    }

    return render(request, 'index.html', context)


def comments(request):
    all_comments = Comments.objects.order_by('-date_created')[:8]

    context = {
        'all_comments' : all_comments
    }

    return render(request, "comments.html", context)
