FROM python:3.5.0-onbuild

RUN pip install uWSGI

EXPOSE 80

CMD ["uwsgi", "--ini", "uwsgi.ini:production"]
