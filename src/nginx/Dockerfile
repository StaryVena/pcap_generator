FROM nginx:alpine
RUN apk add --update --no-cache tcpdump && rm -rf /var/cache/apk/*

VOLUME  [ "/tcpdump" ]

COPY script.sh /script.sh
COPY mysite.template /etc/nginx/conf.d/default.conf