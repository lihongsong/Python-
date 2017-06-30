# -*- coding:utf-8 -*-

from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import sleep,ctime

lock = Lock()

MAX = 5

candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print("refill candy...")
    try:
        candytray.release()
    except ValueError:
        print("full skipping")
    else:
        print("refill candy OK")
    lock.release()

def buy():
    lock.acquire()
    print("buy candy")
    if candytray.acquire(False):
        print("buy candy OK")
    else:
        print("epmty, skipping")
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def customer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def main():
    nloops = randrange(2,6)
    t1 = Thread(target=producer,args=(randrange(nloops,nloops + MAX + 2),))
    t2 = Thread(target=customer,args=(nloops,))
    t1.start()
    t2.start()

@register
def _atexit():
    print("all done at :",ctime())

if __name__ == "__main__":
    main()
