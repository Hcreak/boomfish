FROM centos

RUN yum -y upgrade

RUN mkdir /boomfish
ADD db /boomfish/db
ADD static /boomfish/static
ADD templates /boomfish/templates
ADD boomfish.py /boomfish/boomfish.py

RUN yum -y install python python-devel pip nginx
RUN pip install uwsgi flask
ADD nginx.conf /etc/nginx/nginx.conf
ADD uwsgi.ini /boomfish/uwsgi.ini

EXPOSE 80

ADD start.sh /boomfish/start.sh
WORKDIR /boomfish
CMD ["./start.sh"]