from django.conf.urls import url,include
from persistentchat.views import *

urlpatterns = [
		url(r'^main', mainView, name="main view"),
]
