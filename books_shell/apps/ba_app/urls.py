from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<book_id>\d+)$', views.view),
    
    
]