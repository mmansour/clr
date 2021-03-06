from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from ytdata.models import YouTuber
import urllib2
import requests
import time
from settings import UA

class Command(BaseCommand):
    help = 'Get all facebook likes'
    def handle(self, *args, **options):

        yt = YouTuber.objects.exclude(facebook_url__isnull=True).exclude(facebook_url__exact='')

        for user in yt:
            time.sleep(1)
            fburldb = YouTuber.objects.get(title=user.title)
            try:
                if user.facebook_url[:4] != 'http':
                    clean_url = 'http://{0}'.format(user.facebook_url)
                else:
                    clean_url = user.facebook_url
                fbpage=requests.get(clean_url, headers=UA)
#                fbpage=urllib2.urlopen(clean_url)
                fbsoup=BeautifulSoup(fbpage.text)
                fbsociallink=fbsoup.findAll('meta',{'name':'description'})
                fbdigitlist = [s for s in fbsociallink[0]['content'].split()
                                    if s.replace(",","").isdigit()]
    #                        print k, fbdigitlist, fbsociallink[0]['content']
                fburldb.facebook_likes = fbdigitlist[0].replace(',','')
                print 'User: {0}, Likes: {1} Url: {2}'.format(user.title, fbdigitlist[0], clean_url)
            except IndexError, e:
                fburldb.facebook_error = 'Missing Likes: {0}'.format(e)
                print 'User: {0}, Missing Likes: {1}'.format(user.title, e)
            except urllib2.HTTPError, e:
                fburldb.facebook_error = 'FB Page not found: {0}'.format(e)
                print 'User: {0}, FB Page not found: {1}'.format(user.title, e)
            except urllib2.URLError, e:
                fburldb.facebook_error = 'URL Error: {0}'.format(e)
                print 'User: {0}, URL Error: {1}'.format(user.title, e)
            except UnicodeEncodeError, e:
                fburldb.facebook_error = 'Weird characters in url: {0}'.format(e)
                print 'Weird characters in url: {0}'.format(e)
            except ValueError, e:
                fburldb.facebook_error = 'Invalid Number: {0}'.format(e)
                print 'Invalid Number: {0}'.format(e)
            finally:
                fburldb.save()

        print 'Done pulling Facebook Likes'
  