from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from activity.models import Points

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Points.objects.all().order_by("-date")[:25],
                                            template_name="activity/activity.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Points,
                                                         template_name = 'activity/Points.html'))]
