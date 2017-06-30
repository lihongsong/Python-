# -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import threading
from time import sleep, ctime
from random import randint

def loop0():
    print(threading.current_thread())
    print("start loop 0 at :",ctime())
    # 当前线程暂停
    sleep(randint(0,4))
    print("loop 0 done at :",ctime())
    return "loop0"

def main():
    print("starting at :",ctime())

    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            future = executor.submit(loop0)

    print("all done at :",ctime())

if __name__ == "__main__":
    main()
