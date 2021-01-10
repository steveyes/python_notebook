import argparse


def default_demo():
    # All optional arguments and some positional arguments may be omitted at the command line.
    # The default keyword argument of add_argument(), whose value defaults to None,
    # specifies what value should be used if the command-line argument is not present.
    # For optional arguments, the default value is used when the option string was not present at the command line:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default=11)
    args = parser.parse_args(['--foo', '12'])
    print(args)
    args = parser.parse_args([])
    print(args)

    # If the default value is a string, the parser parses the value as if it were a command-line argument.
    # In particular, the parser applies any type conversion argument,
    # if provided, before setting the attribute on the Namespace return value.
    # Otherwise, the parser uses the value as is:
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', default='10', type=int)
    parser.add_argument('--width', default=10.5, type=int)
    args = parser.parse_args()
    print(args)

    # For positional arguments with nargs equal to ? or *,
    # the default value is used when no command-line argument was present:
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', nargs='?', default=11)
    args = parser.parse_args(['a'])
    print(args)
    args = parser.parse_args([])
    print(args)

    # Providing default=argparse.SUPPRESS causes no attribute to be added if the command-line argument was not present:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default=argparse.SUPPRESS)
    args = parser.parse_args()
    print(args)
    args = parser.parse_args(['--foo', '11'])
    print(args)
