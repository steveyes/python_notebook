import inspect
import os


def whoami():
    return inspect.stack()[1][3]


def is_root(exit_if_failed=True):
    print(whoami())
    if os.geteuid() == 0:
        return True
    elif os.geteuid() != 0:
        print("not run as root!")
        if exit_if_failed:
            exit(-1)
        else:
            return False
    else:
        print('error run os.geteuid()')
