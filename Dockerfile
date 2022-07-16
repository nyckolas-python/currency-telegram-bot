FROM python:3.8

RUN mkdir -p /app/

WORKDIR /app/

COPY . /app/

CMD [ "make run" ]