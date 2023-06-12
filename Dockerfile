FROM python:3.8-alpine3.17

WORKDIR /python

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3"]