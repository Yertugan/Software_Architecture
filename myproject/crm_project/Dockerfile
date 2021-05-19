FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN pip install django djangorestframework psycopg2

COPY . /code

WORKDIR /code