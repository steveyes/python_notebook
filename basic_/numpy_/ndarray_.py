import numpy as np


def basics_():
    arr = np.array([[1, 2, 3],
                    [4, 2, 5]])
    print('Array is of type: ', type(arr))
    print('No. of dimensions: ', arr.ndim)
    print('Shape of array: ', arr.shape)
    print('Size of array: ', arr.size)
    print('Array stores elements of type: ', arr.dtype)


def create_():
    # creating array from list with type float
    a = np.array([[1, 2, 4], [5, 8, 7]], dtype='float')
    print('Array created using passed list:\n', a)

    # creating array from tuple
    b = np.array((1, 3, 2))
    print('Array created using passed tuple:\n', b)

    # creating a 3*4 array with all zeros
    c = np.zeros((3, 4))
    print('\nAn array initialized with all zeros:\n', c)

    # creating a 4*3 array with all ones
    d = np.ones((4, 3))
    print('\nAn array initialized with all ones:\n', d)

    # create a constant value array of complex type
    e = np.full((3, 3), 6 + 6j, dtype='complex')
    print('\nAn array initialized with all 6s. Array type is complex:\n', e)

    # create a sequential array
    f = np.linspace(-1, 2, 5)
    print('\nAn array start from -1 end with 2, contains 5 elements:\n', f)


def indexing_():
    # An exemplar array
    arr = np.array([[-1, 2, 0, 4],
                    [4, -0.5, 6, 0],
                    [2.6, 0, 7, 8],
                    [3, -7, 4, 2.0]])

    # slicing array
    temp = arr[:2, ::2]
    print('Array with first 2 rows and alternate columns(0 and 2):\n', temp)

    # integer array indexing example
    temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
    print('\nElements at indices (0, 3), (1, 2), (2, 1), (3, 0):\n', temp)

    # boolean array indexing example
    cond = arr > 0
    temp = arr[cond]
    print('\nElements greater than 0:\n', temp)


def basic_operations_():
    a = np.array([1, 2, 5, 3])
    print('adding 1 to every element: ', a + 1)
    print('substracting 3 from each element: ', a - 3)
    print('multiplying each element by 10: ', a * 10)
    print('squaring each element: ', a ** 2)

    # modify this array instance
    a *= 2
    print('doubled each element of original array: ', a)

    # transpose of array
    a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
    print('\noriginal array:\n', a)
    print('\nTranspost of array:\n', a.T)


def unary_operators_():
    arr = np.array([[1, 5, 6],
                    [4, 7, 2],
                    [3, 1, 9]])

    print('Largest element is:', arr.max())

    print('Row-wise maximum elements:', arr.max(axis=1))
    print('Column-wise minimum elements:', arr.min(axis=0))

    print('Sum of all array elements:', arr.sum())
    print('Cumulative sum along each row:\n', arr.cumsum(axis=1))


def binary_operators_():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[4, 3], [2, 1]])
    print('arrays sum:\n', a + b)
    print('array multiplication:\n', a * b)
    print('matrix multiplication:\n', a.dot(b))


def universal_functions_():
    # create a array of sine values
    a = np.array([0, np.pi / 2, np.pi])
    print('sine values of array elements: ', np.sin(a))

    # exponential values
    a = np.array([0, 1, 2, 3])
    print('exponent of array elements:', np.exp(a))

    # square root of array values
    print('square root of array elements: ', np.sqrt(a))


if __name__ == '__main__':
    # basics_()
    # create_()
    # indexing_()
    # basic_operations_()
    # unary_operators_()
    # binary_operators_()
    universal_functions_()
