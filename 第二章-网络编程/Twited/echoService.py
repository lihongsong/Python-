from twisted.internet import reactor,protocol
from twisted.protocols import basic

class EchoProtocol(basic.LineReceiver):
    def lineReceived(self,line):
        if line=='quit':
            self.sendLine("Goodbye.")
            self.transport.loseConnection()
            print("Goodbye. "+ self.transport.getPeer().host)
        else:
            self.sendLine("You said: "+line)
            print("You said: "+line)

    def dataReceived(self,data):
        data = data.decode("utf-8")
        if data == 'quit':
            self.sendLine("Goodbye.".encode("utf-8"))
            self.transport.loseConnection()
        else:
            self.sendLine(("You said: "+ data).encode("utf-8"))

    def connectionMade(self):
        print("connected from %s " % self.transport.getPeer().host)

class EchoServerFactory(protocol.ServerFactory):
    protocol = EchoProtocol

if __name__=="__main__":
    port = 5001
    reactor.listenTCP(port,EchoServerFactory())
    reactor.run()
