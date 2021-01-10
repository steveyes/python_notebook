from flask import Flask
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    'alice': 'alice_password',
    'bob': 'bob_password',
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    return 'Hello, %s!' % auth.username()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
