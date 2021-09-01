from django.shortcuts import render, redirect

from infoScrapper.scrape import PDScrapper, NationScrapper
from news.models import Story 
# from scrape import PDScrapper, NationScrapper


# Create your views here.

def get_news():
    people_daily = PDScrapper('https://www.pd.co.ke/')
    pd_news = people_daily.scrape_data()

    nation_media = NationScrapper('https://nation.africa/kenya')
    nation_news = nation_media.scrape_data()

    return (pd_news, nation_news)

def save_news():
    current_news = get_news()
    #unpacking to media sites
    pd_news = current_news[0]
    nation_news = current_news[1]

    for story in pd_news:
        Story.objects.create(
            Title = story[0],
            source = 'People Daily',
            source_url = story[1],
            img_url = story[2],
            category = story[3]
        )
    
    for story in nation_news:
        Story.objects.create(
            Title = story[0],
            source = 'Nation Media',
            source_url = story[1],
            img_url = story[2],
            category = story[3]
        )


    


