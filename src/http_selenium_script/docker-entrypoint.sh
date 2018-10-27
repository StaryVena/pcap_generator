#!/bin/sh

sleep 5

selenium-side-runner -c "chromeOptions.args=['headless','disable-gpu','no-sandbox']" --output-directory /root/out /sides/*.side
