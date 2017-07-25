from django.conf.urls import url
from testurlapp import views

urlpatterns = [
    url(r'^user/(?P<month>\d{2})/(?P<year>\d{4})/$', views.home, name='home'),
]
