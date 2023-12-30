FROM ubuntu:20.04

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install python3-dev  build-essential nano

RUN apt-get -y install python3-pip  git curl 

RUN mkdir -p website

WORKDIR /website

COPY . /website/

RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate

CMD uvicorn website.asgi:application --host 0.0.0.0 --port 8005