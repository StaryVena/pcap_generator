FROM python:3.6-alpine3.7

RUN apk --update --no-cache add --update nodejs nodejs-npm
RUN npm install -g selenium-side-runner

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk --update --no-cache add chromium chromium-chromedriver


ADD docker-entrypoint.sh /opt/bin/docker-entrypoint.sh
RUN chmod +x /opt/bin/docker-entrypoint.sh

RUN mkdir /sides

WORKDIR /root

VOLUME [ "/sides" ]


CMD "/opt/bin/docker-entrypoint.sh"
