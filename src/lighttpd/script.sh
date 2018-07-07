#!/bin/bash

rc-service lighttpd start & /usr/sbin/tcpdump -C 1000 -v -i any -w /tcpdump/apache.pcap