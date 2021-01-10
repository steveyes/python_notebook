from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
token_serializer = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'], expires_in=3600)

auth = HTTPTokenAuth(scheme='Bearer')

users = ['alice', 'bob']
for user in users:
    token = token_serializer.dumps({'username': user}).decode('utf-8')
    print('*** token for {}: \n{}\n'.format(user, token))


@auth.verify_token
def verify_token(token):
    g.user = None
    try:
        data = token_serializer.loads(token)
    except:
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False


@app.route('/')
@auth.login_required
def index():
    return 'Hello, %s!' % g.user


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
