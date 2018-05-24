#!/bin/bash

/usr/sbin/nginx
/usr/bin/redis-server /etc/redis.conf
/usr/bin/uwsgi --ini /boomfish/uwsgi.ini