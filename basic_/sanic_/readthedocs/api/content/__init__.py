#!/usr/bin/env python3
#


from sanic import Blueprint

from .data import data
from .parameters import parameters
from .types import types

content = Blueprint.group(data, parameters, types, url_prefix='/content')
