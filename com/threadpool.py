#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time
import Queue
from scan.Sscan import superscan

SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()  #调用父类的构造函数
        self.func = func   #传入线程函数逻辑

    def run(self) :
        self.func()

def worker() :
    global SHARE_Q
    while not SHARE_Q.empty():
        item = SHARE_Q.get() #获得任务
        superscan(item)
        time.sleep(1)

def Threadpool(Port,thread1) :
    _WORKER_THREAD_NUM = thread1   #设置线程个数
    global _WORKER_THREAD_NUM
    global SHARE_Q
	
    #print _WORKER_THREAD_NUM
    #print port1,port2
    threads = []
    for task in Port :  #向队列中放入任务
        SHARE_Q.put(task)
        #print task
    for i in xrange(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()