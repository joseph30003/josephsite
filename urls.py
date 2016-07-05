from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index' ),
    url(r'^trials/$', views.get_name, name='getname'),
    url(r'^trials/file/$', views.show_file, name='showfile'),
]