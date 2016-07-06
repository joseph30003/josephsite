from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^trials/$', views.get_menu, name='getmenu'),
	url(r'^trials/validation/$', views.vl_search, name='validation_query'),
	url(r'^trials/validation/result/$', views.vl_result, name='validation_result'),
    url(r'^trials/file/$', views.show_file, name='showfile'),
]