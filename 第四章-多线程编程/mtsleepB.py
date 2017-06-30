# -*- coding:utf-8 -*-

import threading
from time import ctime, sleep
from threading import Lock

loops = [4,2]

# def loop(nloop,nsec,lock):
#     print("start loop %s at :" % nloop,ctime())
#     sleep(nsec)
#     print("loop %s done at :" % nloop,ctime())
#     lock.release()

def loop(nloop,nsec):
    print("start loop %s at :" % nloop,ctime())
    sleep(nsec)
    print("loop %s done at :" % nloop,ctime())

def main():
    print("starting at :",ctime())

    # 加锁的方式

    # locks = []

    # nloops = range(len(loops))

    # for i in nloops:
    #     lock = Lock()
    #     lock.acquire()
    #     locks.append(lock)
    #
    # for i in nloops:
    #     threadTuple = (i,loops[i],locks[i])
    #     print(threadTuple)
    #     t = threading.Thread(target=loop,args=threadTuple)
    #     t.start()
    #
    # for i in nloops:
    #     while locks[i].locked():pass

    # 使用join方法代替加锁的方式
    threadings = []

    nloops = range(len(loops))

    for i in nloops:
        threadTuple = (i,loops[i])
        t = threading.Thread(target=loop,args=threadTuple)
        threadings.append(t)

    for t in threadings:
        t.start()

    for t in threadings:
        # 直到启动的线程终止之前会一直挂起线程，除非给出了timeout(ps: t.join(timeout=None))
        t.join()

    print("all done at :",ctime())

if __name__ == "__main__":
    main()
