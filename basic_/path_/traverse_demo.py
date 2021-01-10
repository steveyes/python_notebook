#!/usr/bin/env python3
#

import sys, os, argparse, datetime, subprocess, textwrap, shutil, signal
import fnmatch

usage_desc = textwrap.dedent("""
traverse and remove all sub-dirs named as 'build' from the given root dir
""")


class VersionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def traverse(root_dir):
    for root, dirs, files in os.walk(root_dir[0], topdown=False):
        for name in dirs:
            if name == 'build':
                path = os.path.join(root, name)
                print('removing', path)
                # shutil.rmtree(path)


def sigterm(signum, frame):
    if signal == signal.SIGTERM or signum == signal.SIGINT:
        print('*** SIGTERM/SIGINT received, exiting...')
        exit(0)


def main():
    if sys.version_info < (3, 0):
        raise VersionError("Python version should be at least 3.0")

    parse = argparse.ArgumentParser()
    parse.add_argument(dest='dir', metavar='dir', nargs='*', help='root dir')
    parse.add_argument('--usage', dest='usage', action='store_true', help='show usage')
    args = parse.parse_args()

    if args.usage is True:
        print(usage_desc)
        exit(0)


    signal.signal(signal.SIGTERM, sigterm)
    signal.signal(signal.SIGINT, sigterm)

    traverse(args.dir)


if __name__ == '__main__':
    main()
