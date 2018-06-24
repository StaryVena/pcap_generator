#!/bin/bash

nginx -g "daemon on;" & /usr/sbin/tcpdump -C 1000 -v -i any -w /tcpdump/tcpdump.pcap