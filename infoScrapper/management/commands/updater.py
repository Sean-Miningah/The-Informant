from django.core.management.base import BaseCommand
from ...views import save_news

class Command(BaseCommand):
    help = "Scrape data from websites"

    def handle(self, *args, **kwargs):
        save_news()