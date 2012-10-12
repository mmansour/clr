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
        }
#        pprint.pprint(most_subscribed.text)


        yt = YouTuber.objects.filter(status=2)

        for u in yt:
            user = requests.get("http://gdata.youtube.com/feeds/api/users/{0}".format(u.title), params=payload)
            jr = json.loads(user.text)
#            pprint.pprint(jr['entry']['media$thumbnail']['url'])
#            update = YouTuber.objects.get(u.title)
#            update.youtube_thumbnail_url = jr['entry']['media$thumbnail']['url']











  