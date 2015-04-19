FROM python:3-onbuild

RUN pip install uWSGI

EXPOSE 80

CMD ["uwsgi", "--ini", "uwsgi.ini:production"]
