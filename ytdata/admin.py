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
                                                 'facebook_shares','twitter_shares',
                                                 'facebook_likes','twitter_followers'
        ]}),
    ]

    list_display = ('title', 'status', 'publish_date',
                    'youtube_total_uploaded_views'
        )
    list_editable = ('status',)
    list_filter = ['title', 'status','publish_date']
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(YouTuber, YouTuberAdmin)
  