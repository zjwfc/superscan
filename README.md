## Superscan 
---

- 基于python2、scapy模块的端口扫描。
- 基于scapy发送、侦听和解析的三次握手

```
$ python superscan.py -h

 ___ _   _ _ __   ___ _ __ ___  ___ __ _ _ __
/ __| | | | '_ \ / _ \ '__/ __|/ __/ _` | '_ \
\__ \ |_| | |_) |  __/ |  \__ \ (_| (_| | | | |
|___/\__,_| .__/ \___|_|  |___/\___\__,_|_| |_|
          |_|
                                   v 1.0.0


Usage: superscan.py [options] target.com

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -s SELECT             Select the scan type.eg: -s TCP/FIN,default is SYNscan
  -i IP                 Target IP.eg: -s www.baidu.com/192.168.0.2
  -P PORT               Scan Port.eg: -P 80,3306
  -p SPORT              Scan Port.eg: -p 80-83
  -t THREAD, --thread=THREAD
                        Thread scan,default is 5,eg: -t 10
  -o OUTPUT, --output=OUTPUT
                        Output file name. default is {target}.txt,eg: -o 1.txt

```