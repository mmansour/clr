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
#            'q':'RayWilliamJohnson'
        }

#        http://gdata.youtube.com/feeds/api/users/RayWilliamJohnson?v=2 #### Gets User Profile
        most_subscribed = requests.get("https://gdata.youtube.com/feeds/api/channels", params=payload)
#        pprint.pprint(most_subscribed.text)
        jr = json.loads(most_subscribed.text)
        pprint.pprint(jr)
#        print r.url
#
#        total_results = jr['feed']['openSearch$totalResults']['$t']
#        number_of_pages = float(total_results) / 10
#        which_page = 0
#        rs_start_index = 1

##########################################################################################

#        def UpdateMostViewed(self, newpayload):
#            newpayload = dict(payload.items() + newpayload.items())
#            r = requests.get("https://gdata.youtube.com/feeds/api/channelstandardfeeds/most_subscribed?v=2", params=newpayload)
#            jr = json.loads(r.text)
#
#            for entry in jr['feed']['entry']:
#            pprint.pprint(entry)
#            entry['author'][0]['name']['$t'] # e.g RayWilliamJohnson
#            entry['author'][0]['yt$userId']['$t']
#            entry['yt$channelId']['$t']
#            entry['author'][0]['uri']['$t'] # Feed URI
#            entry['media$group']['media$thumbnail'][0]['url']
#            entry['media$group']['media$title']['$t'] # Thumbnail caption
#            entry['yt$channelStatistics']['totalUploadViewCount'] # Total Views all Videos
#            entry['yt$channelStatistics']['subscriberCount'] # Subscriber Count
#            entry['yt$channelStatistics']['videoCount'] # number of vids
#            entry['yt$channelStatistics']['viewCount'] # number of views for channel
#            entry['yt$channelStatistics']['commentCount'] # number of comments for channel
#            print entry['author'][0]['name']['$t'], entry['author'][0]['yt$userId']['$t'], entry['author'][0]['uri']['$t']
#                pprint.pprint(entry['yt$channelId']['$t'])
#                try:
#                    yt = YouTuber.objects.get(title=entry['author'][0]['name']['$t'])
#                    yt.youtube_thumbnail_url=entry['media$group']['media$thumbnail'][0]['url']
#                    yt.youtube_thumbnail_alt=entry['media$group']['media$title']['$t']
#                    yt.youtube_total_uploaded_views=int(entry['yt$channelStatistics']['totalUploadViewCount'])
#                    yt.youtube_channel_views=int(entry['yt$channelStatistics']['viewCount'])
#                    yt.youtube_subscribers=int(entry['yt$channelStatistics']['subscriberCount'])
#                    yt.publish_date = datetime.datetime.now()
#                    yt.save()
#                except YouTuber.DoesNotExist:
#                    yt = YouTuber(title=entry['author'][0]['name']['$t'],
#                              youtube_userid=entry['author'][0]['yt$userId']['$t'],
#                              youtube_thumbnail_url=entry['media$group']['media$thumbnail'][0]['url'],
#                              youtube_thumbnail_alt=entry['media$group']['media$title']['$t'],
#                              youtube_api_feed=entry['author'][0]['uri']['$t'],
#                              youtube_channel_id=entry['yt$channelId']['$t'],
#                              youtube_total_uploaded_views=int(entry['yt$channelStatistics']['totalUploadViewCount']),
#                              youtube_channel_views=int(entry['yt$channelStatistics']['viewCount']),
#                              youtube_subscribers=int(entry['yt$channelStatistics']['subscriberCount']),
#                              youtube_channel_comment_count=int(entry['yt$channelStatistics']['commentCount']),
#                              status=2)
#                    yt.save()
#
#
#
#        while which_page < number_of_pages:
#            which_page += 1
#            print 'Which page {0}'.format(which_page)
#            UpdateMostViewed(self, {'start-index':'{0}'.format(rs_start_index),'max-results':'10'})
#            rs_start_index += 10







  