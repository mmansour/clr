from ytdata.models import YouTuber
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin



class YouTuberAdmin(DisplayableAdmin):

    fieldsets = [
        ("YouTuber",                 {'fields': ['title','youtube_channel','youtube_video_id','youtube_network','youtube_views',
                                                 'youtube_subscribers','facebook_likes','twitter_followers',
                                                 'shares','youtube_thumbnail_url',]}),
        ("Published Date",        {'fields': ['publish_date']}),
        ("Published Status",      {'fields': ['status']}),
    ]

    list_display = ('title', 'status', 'publish_date', 'youtube_channel','facebook_likes', 'twitter_followers')
    list_editable = ('status',)
    list_filter = ['title', 'status','publish_date']
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(YouTuber, YouTuberAdmin)
  