from bs4 import BeautifulSoup
from lxml import etree
import requests
import random
from collections import OrderedDict


class Scrapper:
    @staticmethod
    def GET_UA():
        uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
        return random.choice(uastrings)


    def __init__(self, url, content=None):
        self.url = url
        self.content = content
        self.header = {'User-Agent': self.GET_UA()}
        self.source = requests.get(url, headers = self.header).text
        self.soup = BeautifulSoup(self.source, 'lxml')

class PDScrapper(Scrapper):
    def __init__(self, url, content=None):
        super().__init__(url, content)
        

    def scrape_data(self):

        first_column = self.soup.find('section')
        top_cards = []
        other_cards = []

        story_link, story_img, story_title, story_tag = [], [], [], []
        for news in first_column.find_all('div', class_='col-12'):
            try:
                top_card = news.find_all('div', class_='card')
                top_cards.extend(top_card)
            
                for top_card in top_cards:
                    story_link.extend([top_card.a['href']])
                    story_img.extend([top_card.a.img['src']])
                    story_title.extend([top_card.div.a.text])
                    story_tag.extend(['Top News'])


                other_card = news.find_all('div', class_='media')
                other_cards.extend(other_card)
                for  other_card in other_cards:
                    story_link.extend([other_card.a['href']])
                    story_img.extend([other_card.a.img['src']])
                    story_title.extend([other_card.a['title']])
                    story_tag.extend(['Other News'])


                if news == first_column.find_all('div', class_='col-12')[-1]:
                    trending_card = news.find('ul', class_='list-group')
                    tcards = trending_card.find_all('li', class_='list-group-item')

                    for story in trending_card.find_all('li', class_='list-group-item'):
                        story_link.extend([story.h5.a['href']])
                        story_title.extend([story.h5.a.text])
                        story_img.extend([None])
                        story_tag.extend(['Trending News'])
                else:
                    pass

            except Exception as e:
                print(e)

        
        res_story_titles = list(OrderedDict.fromkeys(story_title))

        pd_stories = []
        i = 0
        for res_story_title in res_story_titles:
            pd_story = [res_story_title, story_link[i], story_img[i], story_tag[i]]
            pd_stories.extend([pd_story])
            i+=1


        return tuple(pd_stories)

            
class NationScrapper(Scrapper):
    def __init__(self, url, content=None):
        super().__init__(url, content)

    def scrape_data(self):

        teaser = self.soup.find('section', class_="teasers-row-with-sidebar")
        lcolumns = teaser.find('ul', class_="grid-container")

        count = 0
        story_title, story_tag, story_img, story_link = [], [], [], []
        # column.find_all('ol', class_="article-collection")
        for column in lcolumns.find_all('section', class_="nested-cols"):
            for news in column.find_all('li', class_="headline-teasers_item"):
                story_title.extend([news.a['aria-label']])
                story_link.extend(['https://nation.africa'+ news.a['href']])
                try:
                    story_img.extend(['https://nation.africa'+ news.find('img')['src']])
                except:
                    try:
                        story_img.extend(['https://nation.africa'+ news.find('img')['data-src']])
                    except:
                        story_img.extend([None])
                try:
                    story_tag.extend([news.find('aside', class_="article-metadata").span.text])
                except:
                    story_tag.extend(['Ochunglo'])

        
        res_story_titles = list(OrderedDict.fromkeys(story_title))

        pd_stories = []
        i = 0

        #loop return a  tuple of stories from nation stored in lists
        for res_story_title in res_story_titles:
            pd_story = [res_story_title, story_link[i], story_img[i], story_tag[i]]
            pd_stories.extend([pd_story])
            i+=1

        return tuple(pd_stories)

        # for column in lcolumns.find_all('li', class_="col-1-1 medium-col-1-2 large-col-2-3"):
        #     if column == lcolumns.find_all('li', class_="col-1-1")[0]:
        #        headline_teasers = column.find_all('ol', class_='nested-cols')

        #     # print(headline_teasers[0])
        #     print(len(lcolumns.find_all('li', class_="col-1-1 medium-col-1-2")))
        #     print(column)

if __name__ == "__main__":
    main()