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

def write_comment(request):
    all_comments = Comments.objects.order_by('-date_created')
    user_id = request.user.id
    if user_id == None:
        return redirect('top_page')
    else:
        user_comments = Comments.objects.filter(user_id=user_id).order_by('-date_created')
        user = User.objects.get(id=user_id)

        if request.method == "POST":
            if request.user.is_authenticated:
                comment_section = request.POST['comment_section']
                new_comment = Comments.objects.create(
                    comment_content = comment_section,
                    user_id = request.user 
                )
                return redirect('comments_page')
            else:
                redirect('login')
        elif request.method == "GET":

            context = {
                'all_comments' : all_comments,
                'user' : user,
                'user_comments' : user_comments
            }
            return render(request, 'add_comment.html', context)

def dashboard(request):
    tags = Story.objects.values_list('category').distinct()
    if request.method == "POST":
        stag = request.POST['selected_tag']
        stories = Story.objects.filter(category=stag)
        context = {
            'stories': stories,
            'tags': tags,
        }
        print(stories)
        return render(request, 'news_tags.html', context)
    elif request.method == "GET":
        stories = Story.objects.all().order_by('-Datetime')
        context = {
            'tags' : tags,
            'stories' : stories,
        }
        return render(request, 'news_tags.html', context)
