from django.core.management.base import BaseCommand, CommandError
import gdata.youtube
import gdata.youtube.service
from ytdata.models import YouTuber
import requests
from BeautifulSoup import BeautifulStoneSoup
import pprint
import json

class Command(BaseCommand):
    help = 'Pulls most viewed channels from youtube'
    def handle(self, *args, **options):

        payload = {
            'key': 'AI39si6iPjtPqQVnI5NEVOqo28NnV-Xzojm58Ui7BKU9-XmXDHr80YhCeXKyViIoDTEwgQz5C4VcNd7Qd-vMPItVh73HUEeAwA',
            'alt':'json'
        }
        r = requests.get("https://gdata.youtube.com/feeds/api/channelstandardfeeds/most_subscribed?v=2", params=payload)
        jr = json.loads(r.text)

        total_results = jr['feed']['openSearch$totalResults']['$t']
        number_of_pages = float(total_results) / 25
        which_page = 0
        rs_start_index = 1

        pprint.pprint(jr)


#        pprint.pprint(len(jr['feed']['entry']))


#        ################################################ python-gdata-client########################################

#        uri = "https://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?v=2& \
#                       key=AI39si6iPjtPqQVnI5NEVOqo28NnV-Xzojm58Ui7BKU9-XmXDHr80YhCeXKyViIoDTEwgQz5C4VcNd7Qd-vMPItVh73HUEeAwA& \
#                       start-index=1&max-results=25"
#
#        yt_service = gdata.youtube.service.YouTubeService()
#        feed = yt_service.GetYouTubeVideoFeed(uri)
#
#        total_results = feed.total_results.text
#        number_of_pages = float(total_results) / 25
#        which_page = 0
#        rs_start_index = 1
#
#        print 'total results, ', total_results
#        print 'number of pages, ', number_of_pages
#        print 'which page, ', which_page
#        print 'RS Start Index, ', rs_start_index
#
#        def UpdateMostViewed(self, url):
#            yt_service = gdata.youtube.service.YouTubeService()
#            feed = yt_service.GetYouTubeVideoFeed(url)
#
#            for entry in feed.entry:
#                ytvideoidlist = entry.id.text.split('/')
#                ytvideoid = ytvideoidlist[6] # GET Video ID at End of String
#                print "Video ID %s" % ytvideoid
#                print 'Entry ID: %s' % entry.id.text
#                print 'Author Name: %s' % entry.media.credit.text
#                print 'Video title: %s' % entry.media.title.text
#                print 'Video duration: %s' % entry.media.duration.seconds
#                print 'View Count : %s' % entry.statistics.view_count
#                print 'Video published on: %s ' % entry.published.text
#    #            print 'Video description: %s' % entry.media.description.text
#                print 'Video category: %s' % entry.media.category[0].text
#                print 'Video tags: %s' % entry.media.keywords.text
#                print 'Video watch page: %s' % entry.media.player.url
#                print 'Video flash player URL: %s' % entry.GetSwfUrl()
#                print 'Video duration: %s' % entry.media.duration.seconds
#
#                # non entry.media attributes
#    #            print 'Video geo location: %s' % entry.geo.location()
#                print 'Video rating: %s' % entry.rating.average
#
#                # show alternate formats
#                for alternate_format in entry.media.content:
#                    if 'isDefault' not in alternate_format.extension_attributes:
#                        print 'Alternate format: %s | url: %s ' % (alternate_format.type,
#                                                                 alternate_format.url)
#
#                  # show thumbnails
#                for thumbnail in entry.media.thumbnail:
#                    print 'Thumbnail url: %s' % thumbnail.url
#
#
#                obj, created = YouTuber.objects.get_or_create(title=entry.media.credit.text,
#                                                              youtube_video_id=ytvideoid,
#                                                              youtube_views=entry.statistics.view_count,
#                                                              status=2)
#
#
#        while which_page <= number_of_pages:
#            which_page += 1
#            print "Page {0} Index {1}".format(which_page, rs_start_index)
#            UpdateMostViewed(self, "https://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?v=2&start-index={0}&max-results=25&"
#                       "key=AI39si6iPjtPqQVnI5NEVOqo28NnV-Xzojm58Ui7BKU9-XmXDHr80YhCeXKyViIoDTEwgQz5C4VcNd7Qd-vMPItVh73HUEeAwA&".format(rs_start_index))
#            rs_start_index += 25
#
#
#        print "Done updating database"



