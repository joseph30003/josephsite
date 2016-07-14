from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^trials/$', views.get_menu, name='getmenu'),
	url(r'^validation/$', views.vl_search, name='validation'),
	url(r'^validation/result/$', views.vl_result, name='validation_result'),
    url(r'^trials/file/$', views.show_file, name='showfile'),
	url(r'^validation/file/$', views.vl_question, name='submittion'),
	url(r'^test/$', views.vl_query, name='queryDemo'),
	url(r'^test/(?P<queryID>[0-9]+)/$', views.vl_questionary, name='questionary'),
	url(r'^test/(?P<queryID>[0-9]+)/(?P<nct>\w+)/$', views.vl_Aws, name='submitAws'),
    url(r'^test/result/$', views.vl_result, name='demoResult'),

]