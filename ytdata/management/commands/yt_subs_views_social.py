from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from ytdata.models import YouTuber
import urllib2
import re
import time
import datetime
from settings import TOP_100_URL, UA
import requests
from urlparse import urlparse
import pprint

class Command(BaseCommand):
    help = 'Pulls stats from youtube'
    def handle(self, *args, **options):
        social_data_dict = {}
        socialkeywords = ['facebook', 'twitter']
        exactMatch = re.compile(r'\b%s\b' % '\\b|\\b'.join(socialkeywords), flags=re.IGNORECASE)
        missing_social_links = []

        yt = YouTuber.objects.filter(status=2)
        for u in yt:
            time.sleep(1)
            datasource=requests.get('http://www.youtube.com/profile?user=%s' % u.title, headers=UA)
#            datasource=urllib2.urlopen('http://www.youtube.com/profile?user=%s' % u.title)
            datasoup=BeautifulSoup(datasource.text)
            
#           ########## UPDATE DATE, SUBS, AND VIEWS
            stats_div = datasoup.findAll('div',{'class':'header-stats'})
            stats_data = stats_div[0].findAll('span',text=True)
            add_stats = YouTuber.objects.get(title=u.title)
            add_stats.publish_date = datetime.datetime.now()
            add_stats.youtube_subscribers = int(stats_data[2].replace(',',''))
            add_stats.youtube_total_uploaded_views = int(stats_data[8].replace(',',''))
            add_stats.save()

#           ########## GET SOCIAL LINKS
            social_link_markup=datasoup.findAll('a',{'class':'yt-uix-redirect-link'})
            social_data_dict[u.title] = [s['href'] for s in social_link_markup if exactMatch.findall(s['href'])]

        for k, v in social_data_dict.iteritems():

            fblist = [i for i in v if 'facebook' in i]
            if len(fblist) > 1 or not fblist:
                pass
            else:
                for fblink in fblist:
                    fburldb = YouTuber.objects.get(title=k)
                    try:
                        if not fburldb.facebook_verified:
                            fburldb.facebook_url = fblink
                    except Exception, e:
                        fburldb.facebook_error = e
                    finally:
                        fburldb.save()

            twitterlist = [t for t in v if 'twitter' in t]
            if len(twitterlist) > 1 or not twitterlist:
                pass
            else:
                for twitlink in twitterlist:
                    twitterurldb = YouTuber.objects.get(title=k)
                    try:
                        if not twitterurldb.twitter_verified:
                            twitterurldb.twitter_url = twitlink
                    except Exception, e:
                        twitterurldb.twitter_error = e
                    finally:
                        twitterurldb.save()

        print "Done getting stats and urls"













    