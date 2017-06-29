#! /usr/bin/python
# -*- encoding: utf-8 -*-

def OUTPUT(scan2,output2):

    if output2 ==None:
	    return
    else:
        with open (output2,"a") as f:
            #f.write(payload)
            scan3 = scan2 + '\n'
            f.write(scan3)
            f.close