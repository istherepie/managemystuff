FROM python:3.5.6-slim

RUN mkdir /application
WORKDIR /application

COPY . /application

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir rethinkdb

EXPOSE 5000