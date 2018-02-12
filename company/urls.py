##################################################
###    Company URLS
##################################################

from django.conf.urls import url
from . import views

app_name = 'company'

urlpatterns = [
    url(r'^$', views.fn_index, name='index'),

]


