#!/usr/bin/env python3
#

import argparse


def main():
    parse = argparse.ArgumentParser(description='Search some files')
    parse.add_argument(dest='filenames', metavar='filename', nargs='*')
    parse.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append',
                       help='text pattern to search for')
    parse.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
    parse.add_argument('-o', dest='outfile', action='store', help='output file')
    parse.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default='slow',
                       help='search speed')
    args = parse.parse_args()
    print(args.filenames)
    print(args.patterns)
    print(args.verbose)
    print(args.outfile)
    print(args.speed)


if __name__ == '__main__':
    main()
