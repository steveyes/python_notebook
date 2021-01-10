import inspect
from numpy import intersect1d, setdiff1d


def if_not(_a, _success_list: list, _failed_list: list):
    if not _a:
        _func_name = f'{inspect.currentframe().f_code.co_name}'
        msg = f'in function {_func_name} : {_a!r}'
        print(msg)
        _success_list.append(f'{_a!r}')
    else:
        _failed_list.append(f'{_a!r}')


def if_is_none(_a, _success_list: list, _failed_list: list):
    if _a is None:
        _func_name = f'{inspect.currentframe().f_code.co_name}'
        msg = f'in function {_func_name} : {_a!r}'
        print(msg)
        _success_list.append(f'{_a!r}')
    else:
        _failed_list.append(f'{_a!r}')


def main():
    values = (
        None,
        False,
        True,
        Ellipsis,
        NotImplemented,
        '',
        list(),
        tuple(),
        set(),
        dict(),
        -1,
        0,
        1,
    )

    if_not_success_list = []
    if_not_failed_list = []
    [if_not(a, if_not_success_list, if_not_failed_list) for a in values]

    if_is_none_success_list = []
    if_is_none_failed_list = []
    [if_is_none(a, if_is_none_success_list, if_is_none_failed_list) for a in values]

    print(f'both success : {intersect1d(if_not_success_list, if_is_none_success_list)}')
    print(f'both failed: {intersect1d(if_not_failed_list, if_is_none_failed_list)}')
    print(f'only success in if_not: {setdiff1d(if_not_success_list, if_is_none_success_list)}')
    print(f'only success in if_is_none: {setdiff1d(if_is_none_success_list, if_not_success_list)}')
    print(f'only failed in if_not: {setdiff1d(if_not_failed_list, if_is_none_failed_list)}')
    print(f'only failed in if_is_none: {setdiff1d(if_is_none_failed_list, if_not_failed_list)}')


if __name__ == '__main__':
    main()
    pass
