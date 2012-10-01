from django.core.management.base import BaseCommand, CommandError
import gdata.youtube
import gdata.youtube.service
#from battles.models import Battle
#from ytdata.youtubeapi import *
#import logging
#logger = logging.getLogger("battles.custom")

class Command(BaseCommand):
    help = 'Pulls most viewed channels from youtube'
    def handle(self, *args, **options):
#        uri = "https://gdata.youtube.com/feeds/api/channelstandardfeeds/US/most_viewed?v=3"
        uri = "https://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?v=2& \
                       key=AI39si6iPjtPqQVnI5NEVOqo28NnV-Xzojm58Ui7BKU9-XmXDHr80YhCeXKyViIoDTEwgQz5C4VcNd7Qd-vMPItVh73HUEeAwA"

        yt_service = gdata.youtube.service.YouTubeService()
        feed = yt_service.GetYouTubeVideoFeed(uri)
        print feed


