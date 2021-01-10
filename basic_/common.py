import functools
import signal
import sys
import datetime
import time
from subprocess import Popen, PIPE

import psutil as psutil


def singleton(cls):
    """Make a class a Singleton class (only one instance)
    by defining like:

        @singleton
        class ClassA():
            pass

    to make it singleton
    """

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper



def epoch_to_human_readable(epoch_in_nanos):
    """how to get current timestamps in nanosencond

        # %s seconds since 1970-01-01 00:00:00 UTC
        # %N nanoseconds (000000000..999999999)
        date +%s%N
    """
    nanos_per_second = 10 ** 9
    seconds = int(epoch_in_nanos) / nanos_per_second
    nanos = int(epoch_in_nanos) % nanos_per_second
    dt = datetime.datetime.fromtimestamp(seconds)
    # > stand for right justify

    # print([f"{str(dt):>0{size}}" for dt, size in
    #        {dt.year: 4, dt.month: 2, dt.day: 2, dt.hour: 2, dt.minute: 2, dt.second: 2, nanos: 9}.items()])
    print('-'.join([f"{str(dt):>0{size}}" for dt, size in {
        dt.year: 4, dt.month: 2, dt.day: 2, }.items()])
          + ' ' +
          ':'.join([f"{str(tm):>0{size}}" for tm, size in {
              dt.hour: 2, dt.minute: 2, dt.second: 2, }.items()])
          + '.' +
          f"{str(nanos):>09}")


def kill_process(max_retry, p_instance: psutil.Process, p_name, kill_process_retry_interval: int = 60):
    if not p_instance:
        return
    count: int = 0
    while psutil.Process(p_instance.pid).status() != psutil.STATUS_ZOMBIE:
        p_instance.terminate()
        time.sleep(kill_process_retry_interval)
        if count % kill_process_retry_interval == 0:
            print(f'terminating process: {p_name}')
        count += 1
        if count > max_retry:
            print(f'reach max limitation of retries and failed to terminate process: {p_name}')
            return

    # clear the zombie
    p_instance.kill()
    p_instance = None
    print(f'{p_name} is terminated')


def sigterm(signum, frame):
    if signum == signal.SIGTERM or signum == signal.SIGINT:
        print('SIGTERM/SIGINT received, exiting...')
        exit(0)


def sig_reg():
    signal.signal(signal.SIGTERM, sigterm)
    signal.signal(signal.SIGINT, sigterm)


def version_required():
    if sys.version_info < (3, 7):
        raise Exception("Python version should be at least 3.7")


def debug(func):
    """print the function signature and return value"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__}({signature}): ")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned: {value!r}")
        print()
        return value

    return wrapper


def analyse_mem():
    from pympler import asizeof
    print(asizeof.asizeof(version_required))


def analyse_time():
    from timeit import timeit
    print(timeit(stmt='ver', setup='ver=version_required("3.7")', globals=globals()))
    print(timeit(stmt='ver', setup='ver=version_required("3.8")', globals=globals()))


def run_shell(command: str, tee_console=True, exit_if_failed=True, ):
    process = Popen(command.split(), stdin=PIPE, stdout=PIPE, shell=True, )
    stdout, stderr = process.communicate()
    returncode = process.returncode
    if tee_console:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
        if exit_if_failed:
            exit(-1)
    return returncode, stdout, stderr


def main():
    if sys.version_info < (3, 8):
        raise Exception("python version should be at least 3.8")

    signal.signal(signal.SIGTERM, sigterm())
    signal.signal(signal.SIGINT, sigterm())


if __name__ == '__main__':
    epoch_to_human_readable(1575254030086532336)
