#!/bin/bash

/usr/sbin/nginx
/usr/bin/redis-server /etc/redis.conf
/usr/bin/python -c 'import boomfish; boomfish.sync_redis()'
/usr/bin/uwsgi --ini /boomfish/uwsgi.ini