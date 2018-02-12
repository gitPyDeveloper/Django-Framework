##################################################
###    MUSIC URLS
##################################################

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.fn_index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.fn_detail, name='detail'),

]

