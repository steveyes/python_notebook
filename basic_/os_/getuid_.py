import os

if __name__ == '__main__':
    if os.getuid() != 0:
        print("must run as root")
        exit(-1)
