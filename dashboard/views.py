from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import services


@login_required
def dashboard(request):
    feeds = services.get_channel_data()
    feed_data = feeds['feeds']
    return render(request, 'dashboard/dashboard.html', {'feed_data': feed_data})
