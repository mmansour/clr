from django.db import models
from mezzanine.core.models import Displayable, RichTextField
from django.utils import simplejson
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from mezzanine.generic.fields import CommentsField, RatingField
from simple_history.models import HistoricalRecords

#Required for south to work with geo django
from south.modelsinspector import add_introspection_rules
rules = [
  (
    (),
    [],
    {
#        "to": ["rel.to", {}],
#        "to_field": ["rel.field_name", {"default_attr": "rel.to._meta.pk.name"}],
#        "related_name": ["rel.related_name", {"default": None}],
#        "db_index": ["db_index", {"default": True}],
    },
  )
]
add_introspection_rules(rules, ["^django\.contrib\.gis"])


# Create your models here.
class YouTuber(Displayable):
    youtube_thumbnail_url = models.CharField(max_length=200, verbose_name="Thumbnail Url", blank=True, null=True)
    youtube_thumbnail_alt = models.CharField(max_length=200, verbose_name="Thumbnail Alt", blank=True, null=True)
    youtube_video_id = models.CharField(max_length=40, verbose_name="Youtube Video ID", blank=True, null=True)
    youtube_userid = models.CharField(max_length=40, verbose_name="Youtube User ID", blank=True, null=True)
    youtube_channel = models.CharField(max_length=200, verbose_name="Channel URL", blank=True, null=True)
    youtube_channel_id = models.CharField(max_length=40, verbose_name="Channel ID", blank=True, null=True)
    youtube_api_feed = models.CharField(max_length=200, verbose_name="API Feed", blank=True, null=True)
    youtube_network = models.CharField(max_length=200, verbose_name="Network", blank=True, null=True)

    youtube_total_uploaded_views = models.BigIntegerField(verbose_name="Youtube Total Uploaded Views", blank=True, null=True)
    youtube_channel_views = models.BigIntegerField(verbose_name="Youtube Channel Views", blank=True, null=True)
    youtube_subscribers = models.BigIntegerField(verbose_name="Youtube Subscribers", blank=True, null=True)
    youtube_channel_comment_count = models.BigIntegerField(verbose_name="Youtube Comment Count", blank=True, null=True)
    facebook_likes = models.BigIntegerField(verbose_name="Facebook likes", blank=True, null=True)
    twitter_followers = models.BigIntegerField(verbose_name="Twitter followers", blank=True, null=True)
    facebook_shares = models.BigIntegerField(verbose_name="Facebook Shares", blank=True, null=True)
    twitter_shares = models.BigIntegerField(verbose_name="Twitter Shares", blank=True, null=True)
    shares = models.BigIntegerField(verbose_name="Twitter followers", blank=True, null=True)

    facebook_url = models.CharField(max_length=200, verbose_name="Facebook Url", blank=True, null=True)
    facebook_verified = models.BooleanField(default=False, verbose_name="Facebook URL Verified ?")
    is_featured = models.BooleanField(default=False, verbose_name="Featured Channel ?")
    
    twitter_url = models.CharField(max_length=200, verbose_name="Twitter Url", blank=True, null=True)
    twitter_verified = models.BooleanField(default=False, verbose_name="Twitter URL Verified ?")

    facebook_error = models.CharField(max_length=200, verbose_name="Facebook Error", blank=True, null=True)
    twitter_error = models.CharField(max_length=200, verbose_name="Twitter Error", blank=True, null=True)

    address1 = models.CharField(max_length=400, verbose_name="Address 1", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City", blank=True, null=True)
    state_province_code = models.CharField(max_length=40, verbose_name="State Province Code", blank=True, null=True)
    postal_code = models.CharField(max_length=40, verbose_name="Postal Code", blank=True, null=True)
    country_code = models.CharField(max_length=40, verbose_name="Country Code", blank=True, null=True)
    latitude = models.CharField(max_length=40, verbose_name="Latitude", blank=True, null=True)
    longitude = models.CharField(max_length=40, verbose_name="Longitude", blank=True, null=True)
    point = models.PointField(null=True, blank=True)
    geomanager = models.GeoManager()
    search_fields = {"title":10, "youtube_channel":10}

    @models.permalink
    def get_absolute_url(self):
        return ('ytdata.views.detail', [self.slug, self.id])

#    def save(self, *args, **kwargs):
#        self.point = Point(float(self.longitude), float(self.latitude))
#        super(YouTuber, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class YouTuberHistory(models.Model):
    youtuber = models.ForeignKey('YouTuber')
    archive_date = models.DateTimeField(_("Archived on"), blank=True, null=True)
    youtube_subscribers = models.BigIntegerField(verbose_name="Youtube Subscribers", blank=True, null=True)
    youtube_total_uploaded_views = models.BigIntegerField(verbose_name="Youtube Total Uploaded Views", blank=True, null=True)
    facebook_likes = models.BigIntegerField(verbose_name="Facebook likes", blank=True, null=True)
    twitter_followers = models.BigIntegerField(verbose_name="Twitter followers", blank=True, null=True)


