#!/bin/sh

sleep 10

cd /home/slavadan/docker

su -m myuser -c "celery -A CatalogProject beat -l info"