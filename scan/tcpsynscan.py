#! /usr/bin/python
# -*- encoding: utf-8 -*-

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

conf.verb=0 # enable verbose mode - Is this actually working?
conf.nofilter=1

def TCPsynscan(IP1,scanport1):
    
	dst_ip = IP1
	src_port = RandShort()

	tcp_syn_scan = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=scanport1,flags='S'),timeout=10)
	# 判断是否收到应答包
	if type(tcp_syn_scan) == type(None):
	    return "[---] %d Port is closed."%scanport1
	# 判断收到的应答包是否具有TCP层
	elif tcp_syn_scan.haslayer(TCP):
	# 判断是否为SYN+ACK数据包
	    if tcp_syn_scan.getlayer(TCP).flags == 0x12:
		    send(IP(dst=dst_ip)/TCP(sport=src_port,dport=scanport1,flags='R'))
            return "[+++]%d Port is open."%scanport1
	# 判断是否为RST数据包
	elif tcp_syn_scan.getlayer(TCP).flags == 0x14:
	    return "[---]%d Port is closed."%scanport1
    # 判断数据包是否具有ICMP层
	elif tcp_syn_scan.haslayer(ICMP): 
           # 判断是否被防火墙过滤
		if tcp_syn_scan.getlayer(TCP).type == 3 and tcp_syn_scan.getlayer(TCP).code in [1,2,3,9,10,13]:
		    return "[---]%d Filtered"%scanport