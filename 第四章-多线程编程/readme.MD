##多线程编程
获取当前线程
threading.current_thread()

#### 对于python虚拟机的访问是由全局解释器锁(GIL)控制的。这个锁就是用来保证同时只有一个线程运行的。

##ThreadPoolExecutor
一个在concurrent.futures模块下的高级库，在任务级别进行操作。异步执行多个任务，知道任务完全完成之后才会继续执行下走。
