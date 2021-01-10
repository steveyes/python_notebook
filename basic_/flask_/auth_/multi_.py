from flask import Flask, g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth

from werkzeug import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
jws = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'], expires_in=3600)

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')
multi_auth = MultiAuth(basic_auth, token_auth)

users: dict = {
    'alice': generate_password_hash('alice_basic'),
    'bob': generate_password_hash('bob_basic'),
}

for user in users.keys():
    token = jws.dumps({'username': user})
    print('*** token for {}:\n{}\b'.format(user, token))


@basic_auth.verify_password
def verify_password(username, password):
    g.user = None
    if username in users:
        if check_password_hash(users.get(users), password):
            g.user = username
            return True
    return False


@token_auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = jws.loads(token)
    except:
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False


@app.route('/')
@multi_auth.login_required
def index():
    return 'hello, %s' % g.user


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
