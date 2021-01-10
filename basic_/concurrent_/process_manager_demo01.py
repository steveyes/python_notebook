from multiprocessing import Process, Manager
import os


def worker(d, l: list):
    d[0] = 0
    d[1] = 1
    d[f"pid{os.getpid()}"] = os.getpid()
    l.append(os.getpid())
    print('----------in worker----------')
    print(d)
    print(l)
    print()


def main():
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(2))

        p_list = []

        jobs = [Process(target=worker, args=(d, l)) for i in range(10)]

        for j in jobs:
            j.start()
        for j in jobs:
            j.join()

        print('----------in main----------')
        print(d)
        print(l)


if __name__ == '__main__':
    main()
