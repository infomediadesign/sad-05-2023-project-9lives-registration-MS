FROM python:3.8-slim-buster

WORKDIR /python

COPY requirements.txt requirements.txt

RUN requirements.txt

COPY . .

CMD [ "python3"]