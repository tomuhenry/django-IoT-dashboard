from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from . import services


@login_required
@cache_page(300)
def dashboard(request):
    feeds = services.get_channel_data()
    feed_data = feeds['feeds']

    for feed in feed_data:
        feed['field1'] = round(float(feed['field1']), 2)

    return render(request, 'dashboard/dashboard.html', {'feed_data': feed_data})
