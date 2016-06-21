from django.shortcuts import render
from django.http.response import HttpResponse
from chat.models import Chat_Room,Message,Chat_User
from django.contrib.auth.decorators import login_required

# Create your views here.

def getRoom(room_name):
	room = [r for r in Chat_Room.objects.all() if r.title==room_name][0]
	return room

def getRoom(room_name):
	room = [r for r in Chat_Room.objects.all() if r.title==room_name][0]
	return room

def getChat_User(request):
		chat_user = [cu for cu in Chat_User.objects.all() if cu.django_user.id == request.user.id][0]
		return chat_user

def getUserColor(request):
		user = getChat_User(request)
		user_color = user.color
		return user_color

@login_required
def view_all_rooms(request):
	chat_rooms = Chat_Room.objects.all()
	context = { "chat_rooms" : chat_rooms }
	return render(request, "chat/all.html", context)

@login_required
def view_room(request, room_name):
	room = getRoom(room_name)
	user_color = getUserColor(request)
	context = { "room" : room, "user_color" : user_color }
	return render(request, "chat/chat_room.html", context)

@login_required
def send_message(request, room_name):
	message_text = request.POST.get("message", "")
	chatuser = getChat_User(request)
	if message_text is not None and message_text != "":
		room = getRoom(room_name)
		if room is not None:
				message = Message()
				message.text = message_text
				message.chat_room = room
				message.chat_user = chatuser
				message.save()
				return HttpResponse("Success")
		return HttpResponse("Invalid Room")
	return HttpResponse("No Message Text")

@login_required
def get_content(request, room_name):
	room = getRoom(room_name)
	if room is not None:
		return HttpResponse("\n".join([m.as_html() for m in room.message_set.all()]))
	return HttpResponse("No room by that name")

@login_required
def get_last_message(request, room_name):
	room = getRoom(room_name)
	if room is not None:
		return HttpResponse([m.as_html() for m in room.message_set.all()][-1])
	return HttpResponse("Invalid Room")
