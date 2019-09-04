FROM python:3.8.0b1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 80

CMD ["uwsgi", "--ini", "uwsgi.ini:production"]
