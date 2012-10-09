from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from ytdata.models import YouTuber
import urllib2
from settings import TOP_100_URL

class Command(BaseCommand):
    help = 'Pulls top 100 subscribed and top 100 viewed channels'
    def handle(self, *args, **options):
        top_100_page=urllib2.urlopen(TOP_100_URL)
        sbtopsoup=BeautifulSoup(top_100_page.read())

        table = sbtopsoup.find('table')
        rows = table.findAll('tr')
        row_count = 0

        for tr in rows:
            row_count += 1
            row = tr.findAll('a',text=True)

            if row_count > 2:
################ GET TOP 100 # OF TOTAL CHANNEL VIEWS
                try:
                    yt = YouTuber.objects.get(title=str(row[6]))
#                    yt.save()
                except YouTuber.DoesNotExist:
                    yt = YouTuber(title=str(row[6]),status=2)
                    yt.save()
                print row[6]












  