from django.shortcuts import render
import datetime, stats.utils, stats.models
from django.db.models import Avg
import json

# Create your views here.
def index(request):
    context = {
        "year": datetime.datetime.now().year,
        "flows": stats.utils.getFlows(),
        "tabularData": stats.utils.getTabularData(),
        "totals": stats.utils.getTotals(),
        "average": int(stats.models.FlowsFIpv4IpTotals.objects.all()[:10].aggregate(Avg('count'))["count__avg"]),
        "att" : stats.utils.getAverageTransmissionTime()
    }
    return render(request, 'stats/index.html', context)