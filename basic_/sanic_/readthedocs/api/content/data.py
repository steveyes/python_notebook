#!/usr/bin/env python3
#

import jpush

from sanic.response import text, json
from sanic import Blueprint

data = Blueprint('data', url_prefix='/data')


# args
# curl http://192.168.250.201:8090/api/content/data/args?name=alice&age=21
@data.route('/args', methods=['GET', ])
async def handler_args(request):
    print(request.args)
    print(request.query_string)
    return json({
        "parsed": True,
        "args": request.args,
        "url": request.url,
        "query_string": request.query_string
    })


# raw_args
# curl http://192.168.250.201:8090/api/content/data/raw_args?name=alice&age=21
@data.route('/raw_args', methods=['GET', ])
async def handler_raw_args(request):
    print(request.raw_args)
    print(request.query_string)
    return json({
        "parsed": True,
        "raw_args": request.raw_args,
        "url": request.url,
        "query_string": request.query_string
    })


# files
# cp /etc/fstab /tmp/fstab; cp /etc/mtab /tmp/mtab
# curl -H "Content-Type:multipart/form-data" -X POST -F "file01=@/tmp/fstab" -F "file02=@/tmp/mtab" http://192.168.250.201:8090/api/content/data/files
# curl -H "Content-Type:multipart/form-data" -X GET -F "file01=@/tmp/fstab" -F "file02=@/tmp/mtab" http://192.168.250.201:8090/api/content/data/files
@data.route('/files', methods=['POST', 'GET', ])
async def handler_files(request):
    print({"files_name": request.files.keys()})
    print({"headers": request.headers['content-type']})

    files_parameters = []
    for file_name, file in request.files.items():
        files_parameters.append({
            "name": file[0].name,
            "type": file[0].type,
            # "body": file[0].body
        })

    return json({
        "received": True,
        "files_name": request.files.keys(),
        "files_parameters": files_parameters,
    })


# form
# cp /etc/fstab /tmp/fstab; cp /etc/mtab /tmp/mtab
# curl -H "Content-Type:multipart/form-data" -X POST -F "file01=fstab" -F "file02=mtab" http://192.168.250.201:8090/api/content/data/form
# curl -H "Content-Type:multipart/form-data" -X GET -F "file01=fstab" -F "file02=mtab" http://192.168.250.201:8090/api/content/data/form
@data.route('/form', methods=['POST', 'GET', ])
async def handler_form(request):
    return json({
        "received": True,
        "form_data": request.form,
        "file02": request.form.get("file02"),
        # "body": request.body
    })


# body
# curl -H "Content-Type:application/json" -X POST -d '{"name":"alice":"age":"21"}' http://192.168.250.201:8090/api/content/data/body
@data.route('/body', methods=['POST', 'GET', ])
async def handler_body(request):
    return text("You are trying to create a user with the following POST: %s" % request.body.decode())
