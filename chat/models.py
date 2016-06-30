from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from datetime import datetime,timedelta
from django.utils import timezone

import re

# Create your models here.
class Color(models.Model):
	title = models.CharField(max_length=50)
	color = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	def getMaterializeClass(self):
		return self.title.lower().replace(" ","-")

	def getDarkened(self,num):
		return self.getMaterializeClass()+" darken-"+str(num)

	def getLightened(self,num):
		return self.getMaterializeClass()+" lighten-"+str(num)
	
	def getDarkened1(self):
		return self.getDarkened(1)

	def getDarkened2(self):
		return self.getDarkened(2)
	
	def getLightened1(self):
		return self.getLightened(1)

	def getLightened2(self):
		return self.getLightened(2)

class Chat_Room(models.Model):
	title = models.CharField(max_length=200)
	color = models.ForeignKey(Color, default=None, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
	    return self.title

	def __repr__(self):
	    return self.__str__()

class Chat_User(models.Model):
	django_user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
	color = models.ForeignKey(Color, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.django_user)

class Message(models.Model):
	text = models.CharField(max_length=500)
	send_date = models.DateTimeField(default = timezone.now)
	chat_room = models.ForeignKey(Chat_Room, on_delete=models.CASCADE)
	chat_user = models.ForeignKey(Chat_User, on_delete=models.CASCADE)
	
	
	def readableDate(self):
		date = self.send_date - timedelta(hours=6)
		return date.strftime("%H:%M:%S %m-%d-%Y")

	link_regex = re.compile(r'(?:(http://)|(www\.))(\S+\b/?)([!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]*)(\s|$)', re.I)
	def URLIFY(self, message_text):
		def replace(match):
			groups = match.groups()
			protocol = groups[0] or ''  # may be None
			www_lead = groups[1] or ''  # may be None
			return '<a href="http://{1}{2}" rel="nofollow">{0}{1}{2}</a>{3}{4}'.format(
				protocol, www_lead, *groups[2:])
		return Message.link_regex.sub(replace, message_text)

	def as_html(self):
		message_text = self.text
		message_text = conditional_escape(message_text)
		message_text = message_text.replace("\r\n", "<br />")
		message_text = message_text.replace("\n", "<br />")
		message_text = self.URLIFY(message_text)
		username = conditional_escape(self.chat_user.django_user.username)
		template_string = """
		<li class=\"\" style=\"color: %s; word-wrap: break-word; text-size: 12px\">
			<span class=\"\" style=\"float: right\">%s</span>
			%s: %s
		</li>
		<div class="divider"></div>
		"""
		return mark_safe(template_string % (self.chat_user.color.color, self.readableDate(), username, message_text))

	def __str__(self):
		return "%s: %s\n%s" % (self.chat_user.django_user.username, self.text, self.send_date)

	def __repr__(self):
	    return self.__str__()

