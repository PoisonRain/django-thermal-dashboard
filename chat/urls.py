from django.conf.urls import url,include
from django.contrib.auth.views import login
from . import views

app_name='polls'
urlpatterns = [
	url(r'^$', views.view_all_rooms, name='view_all_rooms'),
	url(r'^(?P<room_name>[A-Za-z0-9_@ ]+)/$', views.view_room, name='detail'),
	url(r'^(?P<room_name>[A-Za-z0-9_@ ]+)/message$', views.send_message, name='send_message'),
	url(r'^(?P<room_name>[A-Za-z0-9_@ ]+)/get_content$', views.get_content, name='get_content'),
	url(r'^(?P<room_name>[A-Za-z0-9_@ ]+)/get_last_message$', views.get_last_message, name='get_last_message'),
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
	#url(r'^allresults/$', views.allresults, name='allresults'),
	url(r'^captcha/', include('captcha.urls')),
	url(r'^(?P<pk>\d+)/edit_user$', views.chat_user_update.as_view(success_url='/chat'), name='chat_user_update'),
]
