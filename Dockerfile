FROM python:3.5.6-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app.py ./
COPY bootstrap.py ./
COPY datastore.py ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir rethinkdb

CMD [ "gunicorn", "-w 4", "-b :5000", "app:app"]
EXPOSE 5000