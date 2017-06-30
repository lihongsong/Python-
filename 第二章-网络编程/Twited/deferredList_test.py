from twisted.internet import reactor,defer
from ysdeferred import testConnect

def handleAllResult(results,ports):
    for port,resultInfo in zip(ports,results):
        success,result = resultInfo
        if success:
            print("Connected to port %i" % port)

    reactor.stop()

if __name__ == "__main__":

    import sys
    host = sys.argv[1]
    ports = range(1,201)
    testers = [testConnect(host,port) for port in ports]
    # consumeErrors 是否吸收所有错误，否则将会看到错误信息
    defer.DeferredList(testers,consumeErrors=True).addCallback(handleAllResult,ports)
    reactor.run()
