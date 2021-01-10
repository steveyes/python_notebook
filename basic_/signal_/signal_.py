import signal
import time


def signal_ignore():
    # process will be exited 6 seconds later
    signal.alarm(6)

    # sig : SIGINT, handler : ignore
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    signal.pause()


def signal_default():
    # process will be exited 6 seconds later
    signal.alarm(6)

    # sig : SIGALRM, handler : default
    signal.signal(signal.SIGALRM, signal.SIG_DFL)

    signal.pause()


def signal_handler():
    def handler(signum, frame):
        if signum == signal.SIGALRM:
            print("time out")
        elif signum == signal.SIGINT:
            print("Ctrl + c doesn't work")

    signal.alarm(5)
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGALRM, handler)

    while True:
        print("Waiting...")
        time.sleep(2)


if __name__ == '__main__':
    signal_handler()
