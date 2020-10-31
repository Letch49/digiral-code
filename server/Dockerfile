FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir /srv

WORKDIR /srv

COPY requirements.txt /srv/
RUN pip install -r requirements.txt
COPY . /srv/