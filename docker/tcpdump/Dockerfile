FROM alpine

VOLUME  [ "/pcap" ]
RUN apk add --no-cache tcpdump coreutils

# -C file size in MB, -W files max count
CMD [ "-C", "1000", "-W", "10", "-v", "-w", "/pcap/dump" ]
ENTRYPOINT [ "/usr/sbin/tcpdump" ]
