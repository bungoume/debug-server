debug-server
=========

[![Circle CI](https://circleci.com/gh/bungoume/debug-server.svg?style=shield)](https://circleci.com/gh/bungoume/debug-server)
[![Dependency Status](https://gemnasium.com/bungoume/debug-server.svg)](https://gemnasium.com/bungoume/debug-server)
[![License](http://img.shields.io/:license-MIT-blue.svg)](LICENSE)

return server_name, network_route and request_header retortion

![cone-icon](cone-icon.png)

## Description
WebApp for Proxy Test(Load Balancer, Cache). This app return the Request(JSON).

## Demo
https://debug-server.herokuapp.com/

* Attention: Heroku has http proxy and it add optional HTTP Header and change port.

### Sample Response
```
$ http -v https://debug-server.herokuapp.com/ X-My-Delivery-Id:"c3f8aa3a-c886-4499-9d6e-ee29ee477c34"
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: debug-server.herokuapp.com
User-Agent: HTTPie/0.9.2
X-My-Delivery-Id: c3f8aa3a-c886-4499-9d6e-ee29ee477c34



HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
Date: Sun, 22 Mar 2015 16:22:17 GMT
Server: Cowboy
Via: 1.1 vegur

{
    "appname": "bungoume's debug-server on heroku.",
    "body": "",
    "cookies": {},
    "datetime": "2015-03-23T01:22:18.259536+09:00",
    "encoding": null,
    "get": {},
    "hostname": null,
    "meta": {
        "http_accept": "*/*",
        "http_accept_encoding": "gzip, deflate",
        "http_connect_time": "3",
        "http_connection": "close",
        "http_host": "debug-server.herokuapp.com",
        "http_total_route_time": "0",
        "http_user_agent": "HTTPie/0.9.2",
        "http_via": "1.1 vegur",
        "http_x_forwarded_for": "192.0.2.1",
        "http_x_forwarded_port": "443",
        "http_x_forwarded_proto": "https",
        "http_x_my_delivery_id": "c3f8aa3a-c886-4499-9d6e-ee29ee477c34",
        "http_x_request_id": "a2d2c64a-1926-4df5-8653-db1b5a644f4e",
        "http_x_request_start": "1427041338251",
        "remote_addr": "10.216.128.228",
        "server_name": "2e0b9f1d-6e6d-4618-9967-e0704bdcbc1e",
        "server_port": "25676",
        "server_protocol": "HTTP/1.1"
    },
    "method": "GET",
    "path": "/",
    "post": {},
    "uuid": "743707e0-7145-43fb-b7be-28ebd3f9128f"
}
```

## Install
### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Use Docker
#### Docker Hub

```sh
$ sudo docker run -d -p 80:80 bungoume/debug-server
```

#### build container on yourself

```sh
$ git clone https://github.com/bungoume/debug-server.git
$ sudo docker build -t debug-server debug-server
$ sudo docker run -d -p 80:80 debug-server
```

## License

[MIT](LICENSE)


## Author

[bungoume](https://github.com/bungoume)
