from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.shortcuts import render
from django.template import loader


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


def current_datetime(request):
    now = datetime.now()
    t = loader.get_template('current_datetime.html')
    print(request.path)
    print(request.get_host())
    print(request.get_full_path())
    print(request.is_secure())
    values = request.META.items()
    html = []
    for k, v in values:
        html.append((k, v))
    c = {
        'now': now,
        'html': html,
    }
    return HttpResponse(t.render(c, request))



def searh_form(request):
    return render(request, 'searh_form.html')
