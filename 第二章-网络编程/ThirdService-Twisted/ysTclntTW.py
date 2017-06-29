# -*- coding:utf-8 -*-

from twisted.internet import protocol,reactor

HOST = "localhost"
PORT = 21567

class TSClntProtocol(protocol.Protocol):

    def sendData(self):
        data = input("> ")
        if not data:
            self.transport.loseConnection()
        else:
            self.transport.write(data.encode("utf-8"))

    def connectionMade(self):
        self.sendData()

    def dataReceived(self,data):
        print(data)
        self.sendData()

class TSClntFantory(protocol.ClientFactory):

    protocol = TSClntProtocol
    clientConnectionLost = clientCopnnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFantory())
reactor.run()
