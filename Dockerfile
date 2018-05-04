FROM centos

RUN yum -y install epel-release
RUN yum -y upgrade

RUN mkdir /boomfish
ADD db /boomfish/db
ADD static /boomfish/static
ADD templates /boomfish/templates
ADD boomfish.py /boomfish/boomfish.py

RUN yum -y install python python-devel python2-pip nginx gcc
RUN pip install --upgrade pip
RUN pip install uwsgi flask
ADD nginx.conf /etc/nginx/nginx.conf
ADD uwsgi.ini /boomfish/uwsgi.ini

EXPOSE 80

ADD start.sh /boomfish/start.sh
WORKDIR /boomfish
CMD ["./start.sh"]