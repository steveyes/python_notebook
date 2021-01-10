from typing import List
from pizzapy.pizza import Pizza

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10.0),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
]

print('menu.py module name is %s' % __name__)

if __name__ == '__main__':
    print(MENU)

