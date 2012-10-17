from django.core.management.base import BaseCommand, CommandError
from ytdata.models import YouTuber
import requests
import pprint
import json
import datetime
from settings import YOUTUBE_API_KEY

class Command(BaseCommand):
    help = 'Pulls most subscribed channels from youtube'
    def handle(self, *args, **options):

        payload = {
            'v':'2',
            'key': YOUTUBE_API_KEY,
            'alt':'json',
            'region':'US',
            'paid-content':'false',
            'hl':'en',
        }

        movie = requests.get("https://gdata.youtube.com/feeds/api/charts/movies/most_popular", params=payload)

#        pprint.pprint(movie.text)
        jr = json.loads(movie.text)

#        pprint.pprint(jr['feed']['entry'])

        for m in jr['feed']['entry']:
#            print pprint.pprint(m['media$group']['media$title']['$t'])
            print pprint.pprint(m['media$group'])


#
#        yt = YouTuber.objects.filter(status=2)
#
#        for u in yt:
#            movie = requests.get("https://gdata.youtube.com/feeds/api/charts/movies/most_popular", params=payload)
#            jr = json.loads(movie.text)
##            pprint.pprint(jr['entry']['media$thumbnail']['url'])
##            update = YouTuber.objects.get(u.title)
##            update.youtube_thumbnail_url = jr['entry']['media$thumbnail']['url']











    