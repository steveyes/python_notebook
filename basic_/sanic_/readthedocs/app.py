#!/usr/bin/env python3
#


from sanic import Sanic
from .api import api

app = Sanic(__name__)
app.config.from_envvar('CHEKAWA_SETTINGS')
app.blueprint(api)


# 路由
'''
url: The full URL of the request, ie: http://localhost:8090/posts/1/?foo=bar

scheme: The URL scheme associated with the request: http or https

host: The host associated with the request: localhost:8080

path: The path of the request: /posts/1/

query_string: The query string of the request: foo=bar or a blank string ''

uri_template: Template for matching route handler: /posts/<id>/

token: The value of Authorization header: Basic YWRtaW46YWRtaW4=
'''