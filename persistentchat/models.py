from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat_Room(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

class Chat_User(models.Model):
    django_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    color = models.CharField(max_length=200)

class Message(models.Model):
    text = models.CharField(max_length=500)
    send_date = models.DateTimeField('Send Date')
    chat_room = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
    chat_user = models.ForeignKey(Chat_User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s\t%s" % (self.text, self.send_date)

    def __repr__(self):
        return self.__str__()

class Color():
    red = "red"
    blue = "blue"
    green = "green"
    teal = "teal"
    pink = "pink"
    purple = "purple"    
