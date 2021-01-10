#!/usr/bin/env python3
#

from sanic.response import json, text
from sanic import Blueprint

# instantiate
info = Blueprint('info', url_prefix='/info')


# curl http://192.168.250.201:8090/api/info/hello
@info.route('/hello', methods=['GET', ])
async def hello(request):
    return json("hello")


# curl http://192.168.250.201:8090/api/info/world
@info.route('/world', methods=['GET', ])
async def world(request):
    return json("world")


