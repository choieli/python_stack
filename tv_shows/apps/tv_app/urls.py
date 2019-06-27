from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows/$', views.index),
    url(r'^shows/(?P<show_id>\d+)$', views.view),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^shows/new$', views.new),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.delete),

]

