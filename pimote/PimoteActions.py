#!/usr/bin/python

from os import system

class PimoteActions(object):
    pauseKey = "' '"
    ffKey = '^[[C'
    rwKey = '^[[D'
    toggleSubsKey="'s'"
    quitKey="'q'"
    creturn = 'C-m'
    volUpKey = "'='"
    volDownKey = "'-'"

    def __init__(self, user, ipaddress, port):
        self.user = user
        self.ipaddress = ipaddress
        self.port = port

    def escapeCommand(self, command):
        return command
        #return command.replace("'", "\\'")

    def sendCommand(self, command, dry=True):
        command = self.escapeCommand(command)
        print "ssh %s@%s -p %r -t \"%s\"" % (self.user, self.ipaddress, self.port, command)
        if not dry:
            system("ssh " % command)

    def sendKeys(self, keys, dry=True):
        command = "tmux send-keys -t omx %s" % keys
        self.sendCommand(command, dry)

    def playOMX(self, details, dry=True):
        command = "'playOMX %s' %s" % (details, PimoteActions.creturn)
        self.sendKeys(command, dry)

    def playMusic(self, details, dry=True):
        command = "'startNvlc %s' %s" % (details, PimoteActions.creturn)
        self.sendKeys(command)

    def playTwitch(self, details, dry=True):
        command = "'twitch %s' %s" % (details, PimoteActions.creturn)
        self.sendKeys(command)
    
    def pause(self):
        self.sendKeys(PimoteActions.pauseKey)

    def ff(self):
        self.sendKeys(PimoteActions.ffKey)

    def rw(self):
        self.sendKeys(PimoteActions.rwKey)

    def toggleSubtitles(self):
        self.sendKeys(PimoteActions.toggleSubsKey)

    def quit(self):
        self.sendKeys(PimoteActions.quitKey)

    def volumeUp(self):
        self.sendKeys(PimoteActions.volUpKey)

    def volumeDown(self):
        self.sendKeys(PimoteActions.volDownKey)


if __name__ == "__main__":
    pim = PimoteActions('pi', '127.0.0.1', 22)
    pim.sendKeys(PimoteActions.ffKey)
    pim.sendKeys(PimoteActions.rwKey)
    pim.sendKeys(PimoteActions.pauseKey)
    pim.sendKeys(PimoteActions.toggleSubsKey)
    pim.playMusic("yes")
    pim.playOMX("thrones next")
