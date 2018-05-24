#!/bin/bash

/usr/sbin/nginx
/usr/bin/redis-server
/usr/bin/uwsgi --ini /boomfish/uwsgi.ini