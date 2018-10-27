#!/bin/sh

sleep 5

selenium-side-runner -c "browserName=chrome" /sides/*.side
