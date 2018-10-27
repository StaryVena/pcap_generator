FROM node:10-alpine


RUN npm install -g selenium-side-runner

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver xvfb
#RUN apk --update --no-cache add firefox-esr xvfb && rm  -rf /tmp/* /var/cache/apk/*
#COPY ./geckodriver /usr/local/bin/
#RUN chmod a+x /usr/local/bin/geckodriver

ADD docker-entrypoint.sh /opt/bin/docker-entrypoint.sh
RUN chmod +x /opt/bin/docker-entrypoint.sh

RUN mkdir /sides

WORKDIR /root

VOLUME [ "/sides" ]

ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

CMD "/opt/bin/docker-entrypoint.sh"
