from django.shortcuts import render
from django.http import HttpResponse
from PimoteActions import PimoteActions
# Create your views here.

pim = PimoteActions('pi','127.0.0.1', 22)

def pimote(request):
    return render(request, 'pimote/pimote.html', None)

def play(request):
    pim.pause()
    return pimote(request)

def pause(request):
    pim.pause()
    return pimote(request)

def ff(request):
    pim.ff()
    return pimote(request)

def rw(request):
    pim.rw()
    return pimote(request)

def quit(request):
    pim.quit()
    return pimote(request)

def playOMX(request, details):
    pim.playOMX(details)
    return pimote(request)

def playMusic(request, details):
    pim.playMusic(details)
    return pimote(request)

def playTwitch(request, details):
    pim.playTwitch(details)
    return pimote(request)

def volumeUp(request):
    pim.volumeUp()
    return pimote(request)

def volumeDown(request):
    pim.volumeDown()
    return pimote(request)

def toggleSubtitles(request):
    pim.toggleSubtitles()
    return pimote(request)
