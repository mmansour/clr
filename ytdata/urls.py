from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('ytdata.views',
    url("^$", "home", name="home"),
    (r'^youtube-channel-(?P<pageslug>[\w-]+)-(?P<userid>.*)/$', 'detail'),
    (r'^youtube-top-10-subscribed-channels/$', 'yt_top_ten_subs'),
    (r'^youtube-top-50-subscribed-channels/$', 'yt_top_fifty_subs'),
    (r'^youtube-top-100-subscribed-channels/$', 'yt_top_hundred_subs'),

    (r'^youtube-top-10-viewed-channels/$', 'yt_top_ten_viewed'),
    (r'^youtube-top-50-viewed-channels/$', 'yt_top_fifty_viewed'),
    (r'^youtube-top-100-viewed-channels/$', 'yt_top_hundred_viewed'),
    (r'^youtube-movies/most-popular/$', 'yt_top_free_movies'),

    (r'^youtube-stats/$', 'yt_stats_landing'),
)

