#! /usr/bin/python
#! -*-encoding:utf-8 -*-

from scan.tcpscan import TCPscan
from scan.tcpfinscan import TCPfinscan
from scan.tcpsynscan import TCPsynscan
from com.Output import OUTPUT



def type(Type,ip,Output):
    type = Type
    IP = ip
    output = Output
    global type
    global IP
    global output

def superscan(port):
    #print type
    if type == "TCP":
        scan = TCPscan(IP,port)
        OUTPUT(scan,output)
        print scan
    elif type == "FIN":
        scan = TCPfinscan(IP,port)
        OUTPUT(scan,output)
        print scan
    else:
        scan = TCPsynscan(IP,port)
        OUTPUT(scan,output)
        print scan