import gdata.youtube
import gdata.youtube.service
from battles.models import Battle
import time


def GetLatestVideoFeed(uri):
    yt_service = gdata.youtube.service.YouTubeService()
    feed = yt_service.GetYouTubeVideoFeed(uri)

    for entry in feed.entry:

        insecure_swf_url = entry.GetSwfUrl().replace("https", "http") # YOUTUBE JS API NOT WORKING WITH HTTPS
        ytvideoidlist = entry.id.text.split('/')
        ytvideoid = ytvideoidlist[6] # GET Video ID at End of String
        PrintEntryDetails(entry)
        api_date = time.strptime(entry.published.text[:10], "%Y-%m-%d")
        battle, created = Battle.objects.get_or_create(video_youtube_id=ytvideoid,
            defaults={'title':entry.media.title.text, 'video':insecure_swf_url,
                    'publish_date':time.strftime("%Y-%m-%d", api_date),
                    'video_view_count':entry.statistics.view_count, 'status': 1,
                    'question':'Who won?', 'video_youtube_id':ytvideoid})


def UpdateMostViewed(uri):
    yt_service = gdata.youtube.service.YouTubeService()
    feed = yt_service.GetYouTubeVideoFeed(uri)

    for entry in feed.entry:
        insecure_swf_url = entry.GetSwfUrl().replace("https", "http") # YOUTUBE JS API NOT WORKING WITH HTTPS
        ytvideoidlist = entry.id.text.split('/')
        ytvideoid = ytvideoidlist[6] # GET Video ID at End of String
        print ytvideoid
        PrintEntryDetails(entry)

def PrintEntryDetails(entry):
  print 'Entry ID: %s' % entry.id.text
  print 'Video title: %s' % entry.media.title.text
#  print 'View Count : %s' % entry.statistics.view_count
  print 'Video published on: %s ' % entry.published.text
#  print 'Video description: %s' % entry.media.description.text
#  print 'Video category: %s' % entry.media.category[0].text
#  print 'Video tags: %s' % entry.media.keywords.text
#  print 'Video watch page: %s' % entry.media.player.url
#  print 'Video flash player URL: %s' % entry.GetSwfUrl()
#  print 'Video duration: %s' % entry.media.duration.seconds

# non entry.media attributes
#  print 'Video geo location: %s' % entry.geo.location()
  print 'Video view count: %s' % entry.statistics.view_count
#   Rprint 'Video rating: %s' % entry.rating.average

# show alternate formats
#  for alternate_format in entry.media.content:
#    if 'isDefault' not in alternate_format.extension_attributes:
#      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
#                                                 alternate_format.url)

  # show thumbnails
#  for thumbnail in entry.media.thumbnail:
#    print 'Thumbnail url: %s' % thumbnail.url


  print "--- --- --- \n"

#EXAMPLE CALLS
#UpdateMostViewed("http://gdata.youtube.com/feeds/api/users/nicepeter/uploads")
#GetLatestVideoFeed("http://gdata.youtube.com/feeds/api/users/nicepeter/uploads")
#GetLatestVideoFeed("https://gdata.youtube.com/feeds/api/videos?q=Epic+Rap+Battles&author=nicepeter")