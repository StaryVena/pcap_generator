FROM httpd:alpine
RUN apk add --update --no-cache tcpdump && rm -rf /var/cache/apk/*

VOLUME  [ "/tcpdump" ]

COPY script.sh /script.sh
COPY ./example_site /usr/local/apache2/htdocs/