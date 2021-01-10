#!/usr/bin/env python3
#


from sanic.response import json, text
from sanic import Blueprint

# instantiate
bp_api = Blueprint('bp_api')

'''
http reques paremeters
'''


# request parameters

# int
# curl http://192.168.250.201:8090/integer/666
@bp_api.route('/integer/<integer_arg:int>', methods=['GET', ])
async def handler_integer(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


# number
# curl http://192.168.250.201:8090/number/666.666
@bp_api.route('/number/<number_arg:number>', methods=['GET', ])
async def handler_number(request, number_arg):
    return text('Number - {}'.format(number_arg))


# str
# curl http://192.168.250.201:8090/person/alice
@bp_api.route('/person/<name:[A-z]+>', methods=['GET', ])
async def handler_person(request, name):
    return text('Person - {}'.format(name))


# folder
# curl http://192.168.250.201:8090/folder/lib64
@bp_api.route('/folder/<folder_id:[A-z0-9]{0,8}>', methods=['GET', ])
async def handler_folder(request, folder_id):
    return text('Folder - {}'.format(folder_id))


'''
http request types
'''


# post
# curl -X POST -d '{"name":"alice","age":21}' http://192.168.250.201:8090/post
@bp_api.route('/post', methods=['POST', ])
async def handler_post(request):
    return text('POST request - {}'.format(request.json))


# get
# curl http://192.168.250.201:8090/get?name=alice&age=21
@bp_api.route('/get', methods=['GET', ])
async def handler_get(request):
    return text('GET request - {}'.format(request.args))


'''
http request data
'''


# args
# curl http://192.168.250.201:8090/args?name=alice&age=21
@bp_api.route('/args', methods=['GET', ])
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
# curl http://192.168.250.201:8090/raw_args?name=alice&age=21
@bp_api.route('/raw_args', methods=['GET', ])
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
# curl -H "Content-Type:multipart/form-data" -X POST -F "file01=@/tmp/fstab" -F "file02=@/tmp/mtab" http://192.168.250.201:8090/files
# curl -H "Content-Type:multipart/form-data" -X GET -F "file01=@/tmp/fstab" -F "file02=@/tmp/mtab" http://192.168.250.201:8090/files
@bp_api.route('/files', methods=['POST', 'GET', ])
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
# curl -H "Content-Type:multipart/form-data" -X POST -F "file01=fstab" -F "file02=mtab" http://192.168.250.201:8090/form
# curl -H "Content-Type:multipart/form-data" -X GET -F "file01=fstab" -F "file02=mtab" http://192.168.250.201:8090/form
@bp_api.route('/form', methods=['POST', 'GET', ])
async def handler_form(request):
    return json({
        "received": True,
        "form_data": request.form,
        "file02": request.form.get("file02"),
        "body": request.body
    })


# body
# curl -H "Content-Type:application/json" -X POST -d '{"name":"alice":"age":"21"}' http://192.168.250.201:8090/body
@bp_api.route('/body', methods=['POST', 'GET', ])
async def handler_body(request):
    return text("You are trying to create a user with the following POST: %s" % request.body.decode())
