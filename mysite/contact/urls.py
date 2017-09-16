from django.conf.urls import url
from .views import contact, thanks



urlpatterns = [
    url(r'contact_form/$', contact, name='contact'),
    url(r'thanks/$', thanks, name='thanks'),
]
