from django.conf.urls import url

from . import views
# this one needed for json response
# http://localhost:8000/clients/   works
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/', views.ClientList.as_view()),  # returns list of clients
    url(r'^lessons/', views.LessonList.as_view()),  # returns list of lessons
    url(r'^locations/', views.LocationList.as_view()),  # returns list of locations

]