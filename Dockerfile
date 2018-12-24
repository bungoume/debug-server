FROM python:3.7.1-onbuild

EXPOSE 80

CMD ["uwsgi", "--ini", "uwsgi.ini:production"]
