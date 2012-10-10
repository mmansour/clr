from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from ytdata.models import YouTuber, YouTuberHistory
import urllib2
import time

class Command(BaseCommand):
    help = 'Archive previous days stats'
    def handle(self, *args, **options):

        allyt = YouTuber.objects.filter(status=2)

        for u in allyt:
            yt = YouTuber.objects.get(title=u.title)
            
            archive = YouTuberHistory(
                youtuber=yt,
                archive_date=yt.publish_date,
                youtube_subscribers = yt.youtube_subscribers,
                youtube_total_uploaded_views = yt.youtube_total_uploaded_views,
                facebook_likes = yt.facebook_likes,
                twitter_followers = yt.twitter_followers
            )

            archive.save()

        print 'Done Archiving'
