#!/usr/bin/env

FROM cseelye/rpi-nginx-uwsgi-flask:latest

COPY ./app /app

RUN pip install -U -r /app/requirements.txt
