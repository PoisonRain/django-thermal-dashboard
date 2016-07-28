from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from chat.models import Chat_Room,Message,Chat_User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from django_otp.decorators import otp_required

# Create your views here.

@login_required
def game(request):
	return render(request, "gamio/game.html", {})
