#!/usr/bin/env python3
#

from sanic.response import text
from sanic import Blueprint

parameters = Blueprint('parameters', url_prefix='/parameters')


# int
# curl http://192.168.250.201:8090/api/content/parameters/integer/666
@parameters.route('/integer/<integer_arg:int>', methods=['GET', ])
async def handler_integer(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


# number
# curl http://192.168.250.201:8090/api/content/parameters/number/666.666
@parameters.route('/number/<number_arg:number>', methods=['GET', ])
async def handler_number(request, number_arg):
    return text('Number - {}'.format(number_arg))


# str
# curl http://192.168.250.201:8090/api/content/parameters/person/alice
@parameters.route('/person/<name:[A-z]+>', methods=['GET', ])
async def handler_person(request, name):
    return text('Person - {}'.format(name))


# folder
# curl http://192.168.250.201:8090/api/content/parameters/folder/lib64
@parameters.route('/folder/<folder_id:[A-z0-9]{0,8}>', methods=['GET', ])
async def handler_folder(request, folder_id):
    return text('Folder - {}'.format(folder_id))