from django.conf.urls import url, include
from . import views

from history.views import history

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^history/$', history),
    url(r'^contact/$', views.contact, name='contact'),
]
