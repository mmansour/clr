from ytdata.models import YouTuber
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
#from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect

def home(request):
#    top_ten_subs = YouTuber.objects.filter(status=2).order_by('-youtube_subscribers')[:10]
    return render_to_response('index.html',
                       {},
                        context_instance=RequestContext(request))

def yt_stats_landing(request):
#    top_ten_subs = YouTuber.objects.filter(status=2).order_by('-youtube_subscribers')[:10]
    return render_to_response('pages/yt-stats-landing.html',
                       {},
                        context_instance=RequestContext(request))

def yt_top_ten_subs(request):
    top_ten_subs = YouTuber.objects.filter(status=2).order_by('-youtube_subscribers')[:10]
    return render_to_response('pages/yt-top-ten-subs.html',
                       {'top_ten_subs':top_ten_subs},
                        context_instance=RequestContext(request))
