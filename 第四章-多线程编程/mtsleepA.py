# -*- coding:utf-8 -*-

import threading
from time import ctime, sleep

def loop0():
    print("start loop 0 at :",ctime())
    # 当前线程暂停4s
    sleep(4)
    print("loop 0 done at :",ctime())

def loop1():
    print("start loop 1 at :",ctime())
    sleep(2)
    print("loop 1 done at :",ctime())

def main():
    print("starting at :",ctime())
    t1 = threading.Thread(target=loop0)
    t2 = threading.Thread(target=loop1)
    t1.start()
    t2.start()
    sleep(4)
    print("all done at :",ctime())

if __name__ == "__main__":
    main()
