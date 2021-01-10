import math

'''
annotations were introduced in Python 3, and they’ve not been backported to Python 2. 
This means that if you’re writing code that needs to support legacy Python, you can’t use annotations.
Instead, you can use type comments. 
These are specially formatted comments that can be used to add type hints compatible with older code. 
'''


# type comments to function
def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius

# in one line
def headline01(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)


print(headline01("type comments work", width='center'))

# in multiple lines
def headline02(
        text,  # type: str
        width=80,  # type: int
        fill_char="-",  # type: str
):  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)


print(headline02("type comments work", width=40, fill_char=9))


# type comments to variables
pi = 3.142  # type: float

# Run the example through Python and Mypy:
# mypy type_comments.py

