# Helper Functions

from .models import *
import json
import numpy as np

def getFlows():
    flow = []
    query = FlowsFIpv4Totals.objects.all()[120:450] # limit to 100
    for elem in query:
        flow.append([
            elem.sourceipv4address,
            elem.destinationipv4address,
            int(elem.totalbytes),
        ])

    return json.dumps(flow)

def getAverageTransmissionTime():
    query = FlowsFIpv4Subset.objects.all()[:10] # limit to the 10 on display
    values = []
    for elem in query:
        values.append(elem.flowendmilliseconds - elem.flowstartmilliseconds)
    
    return (np.average(values) / 1000000)


def getTabularData():
    return FlowsFIpv4Subset.objects.all()[:100] # limit to 100

def getTotals():
    total = []
    query = FlowsFIpv4IpTotals.objects.all()
    for elem in query:
        total.append([
            elem.ipv4address,
            elem.count
        ])
    return total

