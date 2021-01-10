import argparse
import textwrap


def basic_():
    dash_79 = '-' * 79

    """\
    @prog: program name
    @formatter_class: Passing RawDescriptionHelpFormatter as formatter_class= indicates that description and epilog are already correctly formatted and should not be line-wrapped:
    @description: display in the --help text after usage section
    @epilog: display in the --help text at the bottom
    """

    __description = f"""\
    {dash_79}
    The argparse module makes it easy to write user-friendly command-line interfaces. 
    The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. 
    The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
    ref: https://docs.python.org/3/library/argparse.html
    """

    __epilog = f"""\
    © Copyright 2001-2019, Python Software Foundation.
    {dash_79}
    """
    parser = argparse.ArgumentParser(
        prog=__file__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(__description),
        epilog=textwrap.dedent(__epilog),
    )
    parser.add_argument('-f', '--foo', nargs='?', default='foo01', type=str, help='foo help')
    parser.add_argument('bar', nargs='*', default='bar01', type=str, help='bar help')
    # parser.print_help()

    # args = parser.parse_args(['--foo', 'foo01', 'bar01'])
    args = parser.parse_args()
    print(args)


def fromfile_prefix_chars():
    '''
    Sometimes, for example when dealing with a particularly long argument lists,
    it may make sense to keep the list of arguments in a file rather than typing it out at the command line.
    If the fromfile_prefix_chars= argument is given to the ArgumentParser constructor,
    then arguments that start with any of the specified characters will be treated as files,
    and will be replaced by the arguments they contain.
    For example:
    :return:
    '''
    with open('args.txt', 'w') as fp:
        fp.write("-f\nbar")
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    parser.add_argument('-f')
    args = parser.parse_args(['-f', 'foo', '@args.txt'])
    print(args)


def parents_demo():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent', type=int)

    foo_parser = argparse.ArgumentParser(parents=[parent_parser])
    foo_parser.add_argument('foo')
    args = foo_parser.parse_args(['--parent', '2', 'foo01'])
    print(args)

    bar_parent = argparse.ArgumentParser(parents=[parent_parser])
    bar_parent.add_argument('--bar')
    args = bar_parent.parse_args(['--bar', 'bar01'])
    print(args)


def prefix_char_demo():
    parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+/')
    parser.add_argument('-f')
    parser.add_argument('++bar')
    parser.add_argument('//mar')
    args = parser.parse_args('-f f01 ++bar bar01 //mar mar01'.split())
    print(args)


if __name__ == '__main__':
    basic_()
