from twisted.internet import reactor

from time import ctime

# print("running the reactor")
#
# print("reactor stopped")

def printTime(nloop):
    print("current loop is: %d" % nloop)
    print("current time is: ",ctime())

def stopReactor():
    reactor.stop()

# 设置定时事件
reactor.callLater(1,printTime,1)
reactor.callLater(2,printTime,2)
reactor.callLater(3,printTime,3)
reactor.callLater(4,printTime,4)
reactor.callLater(5,stopReactor)

reactor.run()

print("Reactor stopped")
