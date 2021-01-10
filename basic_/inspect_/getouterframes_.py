import inspect


def get_function_name_from_inside(kind, message):
    frame, filename, line_number, function_name, context, index = inspect.getouterframes(inspect.currentframe())[1]

    print(repr(f'{kind} in function {function_name!r}: {message!r}'))


def foo():
    log = get_function_name_from_inside
    log('error', 'lost connection')
