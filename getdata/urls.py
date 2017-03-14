from django.conf.urls import url

from . import views
# this one needed for json response
# http://localhost:8000/clients/   works
urlpatterns = [
    url(r'^$', views.index, name='index'),
]


