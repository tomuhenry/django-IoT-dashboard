from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from . import services


@login_required
@cache_page(150)
def dashboard_temp(request):
    feeds = services.get_channel_light_data()
    feed_data = feeds['feeds']
    xdata = []
    ydata = []

    for feed in feed_data:
        x = feed['created_at']
        y = feed['field1']
        xdata.append(x)
        ydata.append(y)

    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    feed_data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': "%d %b %Y %H:%M:%S %p",
            'tag_script_js': True,
            'jquery_on_ready': True,
        }
    }
    return render(request, 'dashboard/dashboard.html', feed_data)


@login_required
@cache_page(150)
def dashboard_light(request):
    feeds = services.get_channel_light_data()
    feed_data = feeds['feeds']
    return render(request, 'dashboard/dashboard.html', {'feed_data': feed_data})
