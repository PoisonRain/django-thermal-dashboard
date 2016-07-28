from django.conf.urls import url,include
from django.contrib.auth.views import login
from . import views

app_name='gamio'
urlpatterns = [
	url(r'^$', views.game, name='game'),
]
