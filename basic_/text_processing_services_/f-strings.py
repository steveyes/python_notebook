def multiline_string():
    name = 'alice'
    profession = 'comedian'
    affiliation = 'Monty Python'

    message = f"""\
    Hi {name}.
    You are a {profession}. 
    You were in {affiliation}."""

    print(message)


def speed_test():
    import timeit

    print(timeit.timeit("""\
name = 'Eric'
age = 74
'%s is %s.' % (name, age)""", number=10000))

    print(timeit.timeit("""\
name = 'Eric'
age = 74
'{} is {}.'.format(name, age)""", number=10000))

    print(timeit.timeit("""\
name = 'Eric'
age = 74
f'{name} is {age}.'""", number=10000))


if __name__ == '__main__':
    # multiline_string()
    # speed_test()
    pass
