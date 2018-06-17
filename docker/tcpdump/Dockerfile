FROM alpine

RUN apk add --update --no-cache tcpdump && rm -rf /var/cache/apk/*

VOLUME  [ "/tcpdump" ]

ENTRYPOINT [ "/usr/sbin/tcpdump" ]

# -C file size in MB, -W files max count
CMD [ "-C", "1000", "-W", "10", "-v", "-w", "/tcpdump/dump.pcap" ]