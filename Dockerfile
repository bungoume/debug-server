FROM python:3.4.2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install uWSGI

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN python debug_server/manage.py collectstatic --noinput

EXPOSE 80

CMD ["uwsgi", "uwsgi.ini"]
