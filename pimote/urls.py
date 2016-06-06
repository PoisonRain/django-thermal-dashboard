from django.conf.urls import url
from . import views

app_name='pimote'
urlpatterns = [
    url(r'^$', views.pimote, name='pimote'),
    url(r'^pause/', views.pause, name="pause"),
    url(r'^play/', views.play, name="play"),
    url(r'^ff/', views.ff, name='ff'),
    url(r'^rw/', views.rw, name='rw'),
    url(r'^volumeup/', views.volumeUp, name='volup'),
    url(r'^volumedown/', views.volumeDown, name='voldown'),
    url(r'^togglesubtitles/', views.toggleSubtitles, name='togglesubs'),
    url(r'^quit/', views.quit, name='quit'),
    url(r'^(?P<details>[ a-zA-Z\.\*0-9]+)/playOMX', views.playOMX, name='playOMX'),
    url(r'^(?P<details>[ a-zA-Z\.\*0-9]+)/playMusic', views.playMusic, name='playMusic'),
    url(r'^(?P<details>[ a-zA-Z\.\*0-9]+)/playTwitch', views.playTwitch, name='playTwitch'),
    url(r'^/playOMX', views.pimote, name='playOMX'),
    url(r'^/playMusic', views.pimote, name='playMusic'),
    url(r'^/playTwitch', views.pimote, name='playTwitch'),
    url(r'^(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)/setIpAddress', views.setIpAddress, name='setIpAddress'),
    url(r'^/setIpAddress', views.pimote, name='setIpAddress'),
    url(r'^playPrev', views.playPrev, name='playPrev'),
    url(r'^playNext', views.playNext, name='playNext'),
]
