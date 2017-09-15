from django.http import HttpResponse, Http404
from datetime import datetime, timedelta


def hello(request):
    return HttpResponse('hello, world')


def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.now() + timedelta(hours=offset)
    html = '<html><body>In {}hours, it will be {}.</body></html>'.format(offset, dt)
    return HttpResponse(html)
