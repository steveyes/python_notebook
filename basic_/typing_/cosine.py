import numpy as np # type: ignore
''' appending  
    # type: ignore 
to the import line is same as running following 
mypy --ignore-missing-imports cosine.py
'''


def print_cosine(x: np.ndarray) -> None:
    with np.printoptions(precision=3, suppress=True):
        print(np.cos(x))


x = np.linspace(0, 2 * np.pi, 9)
print_cosine(x)
