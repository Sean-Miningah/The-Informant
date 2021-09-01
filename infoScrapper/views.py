from django.shortcuts import render, redirect

from scrape import PDScrapper, NationScrapper
# from ..news.models import Story 


# Create your views here.

def get_news():
    people_daily = PDScrapper('https://www.pd.co.ke/')
    pd_news = people_daily.scrape_data()

    nation_media = NationScrapper('https://nation.africa/kenya')
    nation_news = nation_media.scrape_data()

    print(f'People daily {type(pd_news[0])}')
    print(type(nation_news))

    return (pd_news, nation_news)

def save_news():
    current_news = get_news()
    #unpacking to media sites
    for current in current_news:
        
        #labeling the news according to source
        if current == current_news[0]:
            pd_stories = current
        elif current == current_news[1]:
            nation_stories = current

        for pd_story in pd_stories:
            print(f"This is {pd_story}\n")
            print(len(pd_stories))


