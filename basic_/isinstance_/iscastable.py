class IsCastable(object):

    def __init__(self, s) -> None:
        self._type = s

    def __call__(self, _type):
        try:
            if isinstance(self._type, bool):
                # exclude True(1.0) and False(0.0)
                return False

            if self._type.lower() in ('nan', 'inf', '-inf'):
                # exclude infinity and  Not-a-Number
                return False

            if isinstance(_type(self._type), _type, ):
                return True

        except ValueError:
            return False


class IsCastableFloat(IsCastable):

    def __call__(self, _type):
        return super().__call__(_type=float)


class IsCastableInt(IsCastable):
    def __call__(self, _type):
        return super().__call__(_type=int)


class IsCastableNumber(IsCastable):
    def __call__(self, _type=None):
        return super().__call__(_type=float) or super().__call__(_type=int)


if __name__ == '__main__':
    print("True")
    print(IsCastableFloat(True)())
    print(IsCastableInt(True)())
    print(IsCastableNumber(True)())

    print("\nFalse")
    print(IsCastableFloat(False)())
    print(IsCastableInt(False)())
    print(IsCastableNumber(False)())

    print('\nnan')
    print(IsCastableFloat('nan')())
    print(IsCastableInt('nan')())
    print(IsCastableNumber('nan')())

    print('\ninf')
    print(IsCastableFloat('inf')())
    print(IsCastableInt('inf')())
    print(IsCastableNumber('inf')())

    print('\n-inf')
    print(IsCastableFloat('-inf')())
    print(IsCastableInt('-inf')())
    print(IsCastableNumber('-inf')())

    print('\nabcde.')
    print(IsCastableFloat('abcde.')())
    print(IsCastableInt('abcde.')())
    print(IsCastableNumber('abcde.')())

    print('\n123.456')
    print(IsCastableFloat('123.456')())
    print(IsCastableInt('123.456')())
    print(IsCastableNumber('123.456')())

    print('\n123')
    print(IsCastableFloat('123')())
    print(IsCastableInt('123')())
    print(IsCastableNumber('123')())
