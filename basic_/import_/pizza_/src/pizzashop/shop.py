"""
The good solution is to avoid the problem – put tests or examples in the package itself and use relative import. 
The dirty solution is to modify sys.path at runtime (yay, dynamic!) by adding the parent directory of the needed package. 
People actually do this despite it’s an awful hack.

As you can see in the first case we have the pizzashop dir in our path and so we cannot find sibling pizzapy package,
while in the second case the current dir src (denoted as '') is in sys.path and it contains both packages.

    (cd ../; python pizzashop/shop.py)
    (cd ../; python -m pizzashop.shop)

"""

import sys

[print(p) for p in sys.path]

import pizzapy.menu

print(pizzapy.menu)
