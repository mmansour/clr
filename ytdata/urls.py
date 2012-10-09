from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('ytdata.views',
    url("^$", "home", name="home"),
    (r'^youtube-top-10-subscribed-channels/$', 'yt_top_ten_subs'),
    (r'^youtube-stats/$', 'yt_stats_landing'),

#    (r'^(?P<pageslug>[\w-]+)-(?P<hotelid>.*)/$', 'detail'),
)

