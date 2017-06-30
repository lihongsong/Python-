# -*- coding:utf-8 -*-

import threading
from time import ctime,sleep


class myThread(threading.Thread):

    def __init__(self,target,args):
        # 调用父类的初始化方法
        super(myThread,self).__init__(target=target,args=args)
        self.target = target
        self.args = args

    def run(self):
        print(threading.current_thread())
        print(threading.active_count())
        self.target(*self.args)


def loop(nloop,nsec):
    print("start loop %s at :" % nloop,ctime())
    sleep(nsec)
    print("loop %s done at :" % nloop,ctime())

def main():

    myThreads = []

    sleepTimes = [4,2]

    print("starting at :",ctime())

    for i in range(len(sleepTimes)):
        t = myThread(target = loop,args = (i,sleepTimes[i]))
        myThreads.append(t)

    for t in myThreads:
        t.start()

    for t in myThreads:
        t.join()

    print(threading.active_count())
    print(threading.current_thread())
    print("all done at :",ctime())

if __name__ == "__main__":
    main()
