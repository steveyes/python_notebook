from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'alice': generate_password_hash('alice123'),
    'bob': generate_password_hash('bob123'),
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
@auth.login_required
def index():
    return 'Hello, %s' % auth.username()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
