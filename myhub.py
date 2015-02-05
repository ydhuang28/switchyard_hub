#!/usr/bin/env python3

'''
Ethernet hub in Python.
'''
from switchyard.lib.address import *
from switchyard.lib.packet import *
from switchyard.lib.common import *

def switchy_main(net):
    # "net" object is used to send and receive packets, and
    # to get information about the network ports/interfaces we have
    my_ports = net.ports() 

    while True:
        try:
            port,packet = net.recv_packet()
        except NoPackets:
            continue
        except Shutdown:
            return

        log_debug ("In {} received packet {} on {}".format(net.name, packet, port))
        # hub functionality goes here


    # graceful shutdown on exit
    net.shutdown()
