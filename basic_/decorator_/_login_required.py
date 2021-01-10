from flask import Flask, g, request, redirect, url_for

import functools

app = Flask(__name__)


def login_required(func):
    """make sure user has logged in before proceeding"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return func(*args, **kwargs)

    return wrapper


@app.route('/secret')
@login_required
def secret():
    pass
