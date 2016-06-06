from django.shortcuts import render
from django.http import HttpResponse
from PimoteActions import PimoteActions
# Create your views here.

class PimoteInstance(object):
    pim = PimoteActions('pi','127.0.0.1', 22)

def pimote(request):
    return render(request, 'pimote/pimote.html', None)

def setIpAddress(request, ip, port):
    ipaddress = str(ip)
    port = int(port)
    PimoteInstance.pim = PimoteActions('pi', ipaddress, port)
    return pimote(request)

def play(request):
    PimoteInstance.pim.pause()
    return pimote(request)

def pause(request):
    PimoteInstance.pim.pause()
    return pimote(request)

def ff(request):
    PimoteInstance.pim.ff()
    return pimote(request)

def rw(request):
    PimoteInstance.pim.rw()
    return pimote(request)

def quit(request):
    PimoteInstance.pim.quit()
    return pimote(request)

def playOMX(request, details):
    PimoteInstance.pim.playOMX(details)
    return pimote(request)

def playMusic(request, details):
    PimoteInstance.pim.playMusic(details)
    return pimote(request)

def playTwitch(request, details):
    PimoteInstance.pim.playTwitch(details)
    return pimote(request)

def volumeUp(request):
    PimoteInstance.pim.volumeUp()
    return pimote(request)

def volumeDown(request):
    PimoteInstance.pim.volumeDown()
    return pimote(request)

def toggleSubtitles(request):
    PimoteInstance.pim.toggleSubtitles()
    return pimote(request)

def playNext(request):
    PimoteInstance.pim.playNext()
    return pimote(request)

def playPrev(request):
    PimoteInstance.pim.playPrev()
    return pimote(request)
