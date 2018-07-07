#!/bin/bash

httpd & /usr/sbin/tcpdump -C 1000 -v -i any -w /tcpdump/apache.pcap