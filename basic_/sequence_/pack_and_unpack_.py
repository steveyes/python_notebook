def list_packing():
    a_int, *a_list = 1, 2,
    print(a_list)

    b_int, *b_list = 1, 2, 3
    print(b_list)

    c_list = 1, 2, 3
    print(c_list)


def tuple_packing():
    a_int, a_tuple = 4, (5,)
    print(a_tuple)

    b_int, b_tuple = 4, (5, 6,)
    print(b_tuple)

    c_tuple = 4, 5, 6
    print(c_tuple)


def list_unpacking():
    [a_int, ] = [1, ]
    print(a_int)
    b1, b2, b3 = [1, 2, 3]
    print(f'{b1},{b2},{b3}')


def tuple_unpacking():
    (a_int,) = (4,)
    print(a_int)
    b1, b2, b3 = (4, 5, 6)
    print(f'{b1},{b2},{b3}')


if __name__ == '__main__':
    list_packing()
    tuple_packing()
    list_unpacking()
    tuple_unpacking()
