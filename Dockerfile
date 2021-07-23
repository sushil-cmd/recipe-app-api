FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.text /requirements.text
RUN pip install -r /requirements.text

WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

