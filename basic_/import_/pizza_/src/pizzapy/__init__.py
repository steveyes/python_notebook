# absolute imports
# from pizzapy.pizza import *
# from pizzapy.menu import *
# relative imports
from .pizza import *
from .menu import *

""" Package init
(cd ../; python -c "import pizzapy")
"""

__all__ = [
    'Pizza',
    'MENU',
]
