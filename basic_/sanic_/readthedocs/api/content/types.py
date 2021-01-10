#!/usr/bin/env python3
#

from sanic import Blueprint
from sanic.response import text

types = Blueprint('types', url_prefix='/types')


# post
# curl -X POST -d '{"name":"alice","age":21}' http://192.168.250.201:8090/api/content/types/post
@types.route('/post', methods=['POST', ])
async def handler_post(request):
    return text('POST request - {}'.format(request.json))


# get
# curl http://192.168.250.201:8090/api/content/types/get?name=alice&age=21
@types.route('/get', methods=['GET', ])
async def handler_get(request):
    return text('GET request - {}'.format(request.args))