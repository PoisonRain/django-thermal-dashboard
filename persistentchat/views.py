from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainView(request):
		return HttpResponse("Main Chat View.")
