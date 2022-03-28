FROM python:3.9

RUN mkdir -p /home/docker
WORKDIR /home/docker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 9090

COPY . /home/slavadan/docker
RUN pip install --no-cache-dir -r requirements.txt