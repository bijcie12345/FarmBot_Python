#!/usr/bin/env

FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
