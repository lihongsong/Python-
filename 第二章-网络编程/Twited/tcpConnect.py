from twisted.internet import reactor,protocol

class QuickDisconnectProtocol(protocol.Protocol):

    def connectionMade(self):
        print("connected to %s " % self.transport.getPeer().host)
        self.transport.loseConnection()

class BasicClientFactory(protocol.ClientFactory):

    protocol = QuickDisconnectProtocol

    def clientConnectionLost(self,connector,reason):
        print("lost connection : %s" % reason.getErrorMessage())
        reactor.stop()

    def clientConnectioFail(self,connector,reason):
        print("connection faild: %s" % reason.getErrorMessage())
        reactor.stop()

reactor.connectTCP("www.baidu.com",80,BasicClientFactory())
reactor.run()
