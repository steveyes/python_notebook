from inspect import currentframe


def get_currentframe(kind, message):
    function_name = currentframe().f_code.co_name

    print(repr(f'{kind} in function {function_name!r}: {message!r}'))


def log(kind, message):
    function_name = currentframe().f_back.f_code.co_name

    print(repr(f'{kind} in function {function_name!r}: {message!r}'))


def main():
    get_currentframe('error', 'lost connection')
    log('error', 'lost connection')


if __name__ == '__main__':
    main()
