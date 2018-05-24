FROM centos

RUN yum -y install epel-release
RUN yum -y upgrade

RUN yum -y install python python-devel python2-pip nginx gcc
RUN pip install --upgrade pip
RUN pip install uwsgi flask
RUN yum -y install redis

RUN mkdir /boomfish
ADD db /boomfish/db
ADD static /boomfish/static
ADD templates /boomfish/templates
ADD boomfish.py /boomfish/boomfish.py

ADD nginx.conf /etc/nginx/nginx.conf
ADD uwsgi.ini /boomfish/uwsgi.ini
ADD redis.conf /etc/redis.conf

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

EXPOSE 80

ADD start.sh /boomfish/start.sh
RUN chmod a+x /boomfish/start.sh
WORKDIR /boomfish
CMD ["./start.sh"]