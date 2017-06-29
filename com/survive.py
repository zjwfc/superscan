#! /usr/bin/python
# -*- encoding: utf-8 -*-

import os
from com.threadpool import Threadpool


def parameter(IP1,port,thread1):
    ip = IP1
    Port = port
    Thread1 = thread1
    global ip
    global Port
    global Thread1
    
    survive()


def survive():
  
    i = os.popen("ping -c 1 "+ip)
    s = str(i.read())
    a = s.find("ttl")
	
    addr=ip.strip().split('.')
	
    if len(addr) != 4:
        print u"ip错误"
    #elif Port1 > Port2:
        #print u"端口输入有误"
    elif a == -1:
        print u"目标主机不可达"+ip
    else :
        Threadpool(Port,Thread1)