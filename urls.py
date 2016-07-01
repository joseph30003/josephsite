from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index' ),
    url(r'^name/$', views.get_name, name='getname'),
    url(r'^name/your-name/$', views.get_name, name='getusername'),
    url(r'^name/file/$', views.show_file, name='showfile'),
]