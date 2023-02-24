FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r /app/requirements.txt

COPY ./assets /app/assets
COPY ./server/*.py /app/server
COPY ./client/main.py /app/client

ENTRYPOINT [ "python3" ]

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]