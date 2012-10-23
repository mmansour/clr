from django.core.management.base import BaseCommand, CommandError
from ytdata.models import YouTuber, YouTubeMovie
import requests
import pprint
import json
import datetime
from django.utils.timezone import utc
from settings import YOUTUBE_API_KEY

class Command(BaseCommand):
    help = 'Pulls most popular movies from youtube'
    def handle(self, *args, **options):
############ MOST POPULAR MOVIES
        payload = {
            'v':'2',
            'key': YOUTUBE_API_KEY,
            'alt':'json',
            'region':'US',
            'paid-content':'false',
            'hl':'en',
            'start-index':'1',
            'max-results':'50'
        }

        movie = requests.get("https://gdata.youtube.com/feeds/api/charts/movies/most_popular", params=payload)

#        pprint.pprint(movie.text)
        jrmovies = json.loads(movie.text)
#        pprint.pprint(jrmovies)
        
#        print jrmovies['feed']['openSearch$totalResults']['$t']
        total_results = jrmovies['feed']['openSearch$totalResults']['$t']
        number_of_pages = float(total_results) / 50
        which_page = 0
        rs_start_index = 1

        def UpdateMostViewed(self):
            for m in jrmovies['feed']['entry']:
#                print pprint.pprint(m['media$group']['media$title'])
                try:
                    clist = ['{0}: {1}'.format(c['$t'], c['role']) for c in m['media$group']['media$credit']]
                    movie_credits = ', '.join(clist)
                except (IndexError, KeyError):
                    movie_credits = 'N/A'

                try:
                    parental_rating = m['media$group']['media$rating'][0]['$t']
                except KeyError:
                    parental_rating = "N/A"

                try:
                    view_count = int(m["yt$statistics"]['viewCount']),
                except KeyError:
                    view_count = (0,)

                try:
                    voter_rating = float(m["gd$rating"]['average'])
                except KeyError:
                    voter_rating = 0

                try:
                    num_voters = int(m["gd$rating"]['numRaters'])
                except KeyError:
                    num_voters = 0

                try:
                    comment_count = int(m["gd$comments"]['gd$feedLink']['countHint'])
                except KeyError:
                    comment_count = 0

                try:
                    movie_url = m['media$group']['media$content'][0]['url']
                except KeyError:
                    movie_url = 'N/A'

                try:
                    movie_thumb = m['media$group']['media$thumbnail'][0]['url']
                except KeyError:
                    movie_thumb = 'N/A'

                try:
                    movie_desc = m['media$group']['media$description']['$t']
                except KeyError:
                    movie_desc = 'N/A'

############### UPDATE MOVIES

                try:
                    the_movie = YouTubeMovie.objects.get(movie_title=m['media$group']['media$title']['$t'])
                    the_movie.view_count=view_count[0]
                    the_movie.voter_rated=voter_rating
                    the_movie.number_of_voters=num_voters
                    the_movie.comment_count=comment_count
                    the_movie.save()
                except YouTubeMovie.DoesNotExist:
                    the_movie = YouTubeMovie(
                        movie_title=m['media$group']['media$title']['$t'],
                        movie_direct_url=movie_url,
                        movie_youtube_url=m['link'][0]['href'],
                        movie_thumbmail_url=movie_thumb,
                        movie_parental_rating=parental_rating,
                        movie_credits=movie_credits,
                        movie_description=movie_desc,
                        view_count=view_count[0],
                        voter_rated=voter_rating,
                        number_of_voters=num_voters,
                        comment_count=comment_count
                    )
                    the_movie.save()


############### GET OR CREATE FOR INIT
#                yt, created = YouTubeMovie.objects.get_or_create(
#                    movie_title=m['media$group']['media$title']['$t'],
#                    movie_direct_url=movie_url,
#                    movie_youtube_url=m['link'][0]['href'],
#                    movie_thumbmail_url=movie_thumb,
#                    movie_parental_rating=parental_rating,
#    #                    movie_restrictions=m['media$group']['media$restriction'][0]['$t'],
#    #                    movie_uploaded_date=m['media$group']['yt$uploaded'],
#                    movie_credits=movie_credits,
#                    movie_description=movie_desc,
#                    view_count=view_count[0],
#                    voter_rated=voter_rating,
#                    number_of_voters=num_voters,
#                    comment_count=comment_count
#                )

                print 'Created movie'

        UpdateMostViewed(self)

#        while which_page <= number_of_pages:
#            which_page += 1
##            UpdateMostViewed(self)
#            rs_start_index += 25
#
#            print which_page, rs_start_index

############ GET CHANNEL/USER/SUBS/VIEWS
#        payload = {
#            'v':'2',
#            'key': YOUTUBE_API_KEY,
#            'alt':'json',
#            'region':'US',
#            'hl':'en',
#        }
#
#        user = requests.get("https://gdata.youtube.com/feeds/api/users/lifeinaday", params=payload)
#
##        pprint.pprint(user.text)
#        jruser = json.loads(user.text)
#        pprint.pprint(jruser)


############ THE DATA I NEED AND HOW TO GET IN IN THE JSON FEED WHERE m IS THE FOR LOOP ITERATOR

#            m['media$group']['media$title']
#            m['media$group']['yt$uploaded'] #date
#            m['media$group']['media$credit'][1]['$t'] #Name IndexError
#            m['media$group']['media$credit'][1]['role'] #Role IndexError
#            m['media$group']['media$description']
#            m['media$group']['media$content'][0]['url'] #the actual movie
#            m['media$group']['media$thumbnail'][0]['url']  thumnails default
#            m['media$group']['media$rating'][0]['$t'] #rating try for KeyError
#            m['media$group']['media$player']['url'] #Also YouTube URL
#            m['link'][0]['href'] # YouTube URL
#            m['media$group']['media$restriction'][0]['$t'] #restriction try for KeyError
#            m['media$group']['yt$videoid']['$t'] #Video ID
#            m["yt$statistics"]["viewCount"] #View Count Key Error
#            m["gd$rating"]['average'] #Movie Voter Rating, KeyError
#            m["gd$rating"]['numRaters'] # How many people rated this
#            m["gd$comments"]['gd$feedLink']['countHint'] # comment count












    