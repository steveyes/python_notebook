import argparse
from os.path import basename

"""actions: 
- store
- store_const
- store_true
- store_false
- append
- append_const
- count
- version
"""


def action_store():
    # 'store'
    # This just stores the argument’s value. This is the default action.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--bar', action='store')
    parser.add_argument('--foo')
    args = parser.parse_args('--bar bar01 --foo foo01'.split())
    print(args)


def action_store_const():
    # 'store_const'
    # This stores the value specified by the const keyword argument.
    # The 'store_const' action is most commonly used with optional arguments that specify some sort of flag.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_const', const='foo02')
    args = parser.parse_args(['--foo'])
    print(args)


def action_store_true():
    # 'store_true' and 'store_false'
    # These are special cases of 'store_const' used for storing the values True and False respectively.
    # In addition, they create default values of False and True respectively.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true')
    parser.add_argument('--bar', action='store_false')
    parser.add_argument('--mon', action='store_false')
    args = parser.parse_args('--foo --bar'.split())
    print(f"mon doesn't parsed, so mon=True")
    print(args)


def action_append():
    # 'append'
    # This stores a list, and appends each argument value to the list.
    # This is useful to allow an option to be specified multiple times.
    # Example usage:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='append')
    args = parser.parse_args('--foo 1 --foo 2'.split())
    print(args)


def action_append_const():
    # 'append_const'
    # This stores a list, and appends the value specified by the const keyword argument to the list.
    # (Note that the const keyword argument defaults to None.)
    # The 'append_const' action is typically useful when multiple arguments need to store constants to the same list.
    # For example:
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='types', action='append_const', const=str)
    parser.add_argument('--int', dest='types', action='append_const', const=int)
    # analog like cmd line: $0 --str --str --int
    args = parser.parse_args('--str --str --int'.split())
    print(args)


def action_count():
    # 'count'
    # This counts the number of times a keyword argument occurs.
    # For example, this is useful for increasing verbosity levels:
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count')
    args = parser.parse_args(['-vvv'])
    print(args)


def action_version_():
    # 'version'
    # This expects a version= keyword argument in the add_argument() call,
    # and prints version information and exits when invoked:
    parser = argparse.ArgumentParser(prog=basename(__file__))
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    args = parser.parse_args(['--version'])
    print(args)


if __name__ == '__main__':
    action_store_true()
