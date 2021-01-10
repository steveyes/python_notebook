import argparse


def nargs_using_num():
    # N (an integer).
    # N arguments from the command line will be gathered together into a list. For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs=2)
    parser.add_argument('bar', nargs=1)
    args = parser.parse_args('c --foo a b'.split())
    print(args)


def nargs_using_question_mark():
    # '?'.
    # One argument will be consumed from the command line if possible, and produced as a single item.
    # Note that for optional arguments, there is an additional case

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs='?', const='c', default='d')
    parser.add_argument('bar', nargs='?', default='d')
    args = parser.parse_args(['xx', '--foo', 'yy'])
    print(args)

    # the option string is present but not followed by a command-line argument.
    # In this case the value from const will be produced.
    args = parser.parse_args(['xx', '--foo'])
    print(args)

    # If no command-line argument is present, the value from default will be produced.
    args = parser.parse_args([])
    print(args)


def nargs_using_asterisk():
    # '*'.
    # All command-line arguments present are gathered into a list.
    # Note that it generally doesn’t make much sense to have more than one positional argument with nargs='*',
    # but multiple optional arguments with nargs='*' is possible.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs='*')
    parser.add_argument('--bar', nargs='*')
    parser.add_argument('mon', nargs='*')
    args = parser.parse_args('a b --foo x y --bar 1 2'.split())
    print(args)


def nargs_using_plus():
    # '+'.
    # Just like '*', all command-line args present are gathered into a list.
    # Additionally, an error message will be generated if there wasn’t at least one command-line argument present.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', nargs='+')
    args = parser.parse_args(['a', 'b'])
    print(args)


def nargs_using_remainder():
    # argparse.REMAINDER.
    # All the remaining command-line arguments are gathered into a list.
    # This is commonly useful for command line utilities that dispatch to other command line utilities:
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo')
    parser.add_argument('command')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args('--foo foo01 cmd01 --arg1 xx yy'.split())
    print(args)


if __name__ == '__main__':
    nargs_using_num()
    # nargs_using_question_mark()
    # nargs_using_asterisk()
    # nargs_using_plus()
    # nargs_using_remainder()
