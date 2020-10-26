#!/usr/bin/env python

FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app
