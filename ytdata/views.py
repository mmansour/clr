from ytdata.models import YouTuber
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect

def home(request):
    top_three_most_subs = YouTuber.objects.filter(status=2).order_by('-youtube_subscribers')[:3]
    top_three_most_viewed = YouTuber.objects.filter(status=2).order_by('-youtube_total_uploaded_views')[:3]
    top_three_featured = YouTuber.objects.filter(status=2).filter(is_featured=True)[:3]


    return render_to_response('index.html',
                       {'top_three_most_subs':top_three_most_subs,
                        'top_three_most_viewed':top_three_most_viewed,
                        'top_three_featured':top_three_featured,},
                        context_instance=RequestContext(request))


def detail(request, pageslug, userid):
    theyoutuber = get_object_or_404(YouTuber, id=userid)
    if pageslug != theyoutuber.slug:
       return HttpResponsePermanentRedirect(theyoutuber.get_absolute_url())
    else:
       return render_to_response('pages/youtuber-detail.html', {'theyoutuber':theyoutuber,},
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


def yt_top_fifty_subs(request):
    top_fifty_subs = YouTuber.objects.filter(status=2).order_by('-youtube_subscribers')[:50]
    return render_to_response('pages/yt-top-fifty-subs.html',
                       {'top_fifty_subs':top_fifty_subs},
                        context_instance=RequestContext(request))


