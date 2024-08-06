# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.12-bullseye AS builder
# user and folder setup
RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/mynt
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

WORKDIR $APP_HOME
COPY ./requirements.txt .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN chown -R app:app $HOME

USER app

RUN python manage.py collectstatic --no-input --clear
