from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from ytdata.models import YouTuber
import urllib2
from settings import TOP_100_URL, UA
import requests

class Command(BaseCommand):
    help = 'Pulls top 100 subscribed and top 100 viewed channels'
    def handle(self, *args, **options):
        top_100_page = requests.get(TOP_100_URL, headers=UA)
#        top_100_page=urllib2.urlopen(TOP_100_URL)
        sbtopsoup=BeautifulSoup(top_100_page.text)
        
        table = sbtopsoup.find('table')
        rows = table.findAll('tr')
        row_count = 0

        for tr in rows:
            row_count += 1
            row = tr.findAll('a',text=True)
            
            if row_count > 2:
################# GET TOP 100 # OF SUBSCIBERS
                yt, created = YouTuber.objects.get_or_create(title=str(row[2]))
                print row[2]
        print top_100_page.headers


        









