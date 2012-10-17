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
#            m['media$group']['media$title']
#            m['media$group']['yt$uploaded']) #date
#            m['media$group']['media$credit'] #list
#            m['media$group']['media$description']
#            m['media$group']['media$content'] #list the actual movie
#            m['media$group']['media$thumbnail'] #list thumnails & "name":default
#            m['media$group']['media$rating'] #list rating try for KeyError
#            m['media$group']['media$player']['url']
#            m['media$group']['media$restriction'] #list restriction try for KeyError
            print pprint.pprint(m['media$group']['yt$videoid']['$t'])


#
#        yt = YouTuber.objects.filter(status=2)
#
#        for u in yt:
#            movie = requests.get("https://gdata.youtube.com/feeds/api/charts/movies/most_popular", params=payload)
#            jr = json.loads(movie.text)
##            pprint.pprint(jr['entry']['media$thumbnail']['url'])
##            update = YouTuber.objects.get(u.title)
##            update.youtube_thumbnail_url = jr['entry']['media$thumbnail']['url']











    