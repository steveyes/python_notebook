from getpass import getpass


def get_credential():
    username = input('username: ')
    password = getpass()
    return username, password
