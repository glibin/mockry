FROM python:3.7-alpine3.7

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
  gcc \
  python3-dev \
  musl-dev \
  libffi-dev

COPY . .

RUN pip3 install --upgrade pip && pip3 install --default-timeout=100 -r requirements.txt
RUN python3 setup.py install

RUN mkdir /data
COPY application.json /data

ENTRYPOINT ["python3", "-m", "mockry", "--host=0.0.0.0", "--json=/data/application.json"]

EXPOSE 7777
