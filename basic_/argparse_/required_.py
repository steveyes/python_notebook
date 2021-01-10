import argparse


def required_demo():
    # In general, the argparse module assumes that flags like -f and --bar indicate optional arguments,
    # which can always be omitted at the command line.
    # To make an option required, True can be specified for the required= keyword argument to add_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', required=True)
    args = parser.parse_args(['--foo', 'BAR'])
    print(args)
    args = parser.parse_args([])
    print(args)
