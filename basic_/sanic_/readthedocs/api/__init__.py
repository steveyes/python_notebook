#!/usr/bin/env python3
#


from sanic import Blueprint
from .content import content
from .info import info

api = Blueprint.group(content, info, url_prefix='/api')
