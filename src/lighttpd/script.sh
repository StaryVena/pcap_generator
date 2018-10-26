#!/bin/sh

/usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf & /usr/sbin/tcpdump -C 1000 -v -i any -w /tcpdump/lighttpd.pcap