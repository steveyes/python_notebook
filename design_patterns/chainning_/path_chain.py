class GetPath(object):
    def __init__(self, path='') -> None:
        # super().__init__()
        self._path = path

    def __getattr__(self, path):
        return GetPath('%s/%s' % (self, path))

    def __call__(self, path):
        return GetPath('%s/%s' % (self, path))

    def __str__(self):
        return self._path


def build_path():
    # the dot: '.' in object().attr invokes the __getattr__(self, attr) of the object
    path01 = GetPath().var.log.nginx
    print(path01)


def append_path():
    # the parentheses '()' in object(para) invokes the __call__(self, para) of the object
    path02 = GetPath()('var')('log')('nginx')
    print(path02)


if __name__ == '__main__':
    # build_path()
    append_path()
