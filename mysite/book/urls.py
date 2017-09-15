from django.conf.urls import url
from .views import search, search_form

urlpatterns = [
    url(r'search/$', search, name='search'),
    url(r'search_form/$', search_form, name='search_form'),
]
