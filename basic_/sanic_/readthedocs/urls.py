#!/usr/bin/env python3
#


from sanic import Sanic
from .views_api import bp_api
from example_.sanic_example.readthedocs import bp_static

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

app = Sanic(__name__)
app.blueprint(bp_api)
app.blueprint(bp_static)
