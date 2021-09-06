# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ADD app.py /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=8080

CMD [ "python3", "./app.py"]