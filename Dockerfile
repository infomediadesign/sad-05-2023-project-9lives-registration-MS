FROM python:3.8-alpine3.17

WORKDIR /python

COPY requirements.txt requirements.txt

RUN requirements.txt

COPY . .

CMD [ "python3"]