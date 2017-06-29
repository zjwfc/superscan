#! /usr/bin/python
# -*- encoding: utf-8 -*-

import socket
from optparse import OptionParser
from com.seting import banner
from com.survive import parameter
#from com.threadpool import Threadpool
from scan.Sscan import type


def main():

    Output = options.output
    thread1 = options.thread
    Type = options.select
    Port = options.port
    Port1 = options.sport
	
    type(Type,IP1,Output)
	
    if Port1 != None:
        port = []
        port1 = Port1.split("-")
        for i in range (int(port1[0]),int(port1[1])):
		    port.append(int(i))
			
        parameter(IP1,port,thread1)   
	
    elif Port == None:
	    port = [80,21,23,22,25,110,443,1080,3306,3389,1521,1433]
	    parameter(IP1,port,thread1)
    else:
        port = []
        port1 = Port.split(",")
        for i in port1:
		    port.append(int(i))
			
        parameter(IP1,port,thread1)

if __name__ == '__main__':

    print banner
	
    optParser = OptionParser('usage: %prog [options] target.com', version="%prog 1.0.0")
    optParser.add_option("-s",action="store", type="string",dest="select",help= 'Select the scan type.eg: -s TCP/FIN,default is SYNscan')
    optParser.add_option("-i", action="store", type="string", dest="ip",help= 'Target IP.eg: -s www.baidu.com/192.168.0.2')
    optParser.add_option("-P", action="store", default = None, type="string", dest="port",help= 'Scan Port.eg: -P 80,3306')
    optParser.add_option("-p", action="store",default = None,type="string", dest="sport",help= 'Scan Port.eg: -p 80-83')
    optParser.add_option("-t",'--thread',action = "store",default = 5 ,type = "int",dest = "thread",help='Thread scan,default is 5,eg: -t 10')
    optParser.add_option("-o", '--output',action = "store",default = None, dest = "output",help= 'Output file name. default is {target}.txt,eg: -o 1.txt')
    options, args = optParser.parse_args()
	
    payload = options.ip
    IP1 = socket.gethostbyname(payload)
	
    
    print "Destination IP ----->"+IP1
    if options.select == "TCP":
        print "*********** Use TCP Scan ***********"
    elif options.select == "FIN":
        print "*********** Use TCP FIN Scan ***********"
    else:
        print "*********** Use TCP SYN scan ***********"

    main()

