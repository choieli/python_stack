from django.conf.urls import url
from.import views

urlpatterns = [
    # url(r'^$',views.index),
    # url(r'^name$',views.name),
    # url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^reset$', views.reset),
    
]