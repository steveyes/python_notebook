#!/usr/bin/env python3
#


import os

from jinja2 import Environment, FileSystemLoader
from sanic import Sanic
from sanic.response import HTTPResponse
from sanic.response import html

app = Sanic(__name__, )
app.static('/static', './static')
base_dir = os.path.abspath(os.path.dirname(__name__))
templates_dir = os.path.join(base_dir, 'templates')
jinja_env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)


def render_template(template_name: str, **context) -> str:
    template = jinja_env.get_template(template_name)
    return template.render(**context)


@app.route('/')
async def index(request) -> HTTPResponse:
    return html(render_template('index.html'))


@app.route('/admin.html')
async def index(request) -> HTTPResponse:
    return html(render_template('admin.html'))


@app.route('/index.html')
async def index(request) -> HTTPResponse:
    return html(render_template('index.html'))


@app.route('/product.html')
async def index(request) -> HTTPResponse:
    return html(render_template('product.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True, access_log=True)
