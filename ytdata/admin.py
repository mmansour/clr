from ytdata.models import YouTuber
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin



class YouTuberAdmin(DisplayableAdmin):

    fieldsets = [
        ("YouTuber",                 {'fields': ['title']}),
        ("Status",      {'fields': ['status']}),
        ("Published Date",        {'fields': ['publish_date']}),
        ("YouTube Data",                 {'fields': ['youtube_channel','youtube_video_id',
                                                 'youtube_network',
                                                 'youtube_total_uploaded_views',
                                                 'youtube_channel_views',
                                                 'youtube_subscribers',
                                                 'shares','youtube_thumbnail_url',
                                                 'facebook_url','twitter_url',
                                                 'facebook_verified','twitter_verified',
                                                 'facebook_likes','twitter_followers',

        ]}),
    ]

    list_display = ('title', 'status', 'publish_date',
                    'youtube_subscribers', 'youtube_total_uploaded_views',
                    'facebook_verified', 'twitter_verified',
                    'facebook_url','twitter_url',
        )
    list_editable = ('status', 'facebook_verified', 'twitter_verified',
                    'facebook_url','twitter_url',)
    list_filter = ['title', 'status','publish_date']
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(YouTuber, YouTuberAdmin)
  