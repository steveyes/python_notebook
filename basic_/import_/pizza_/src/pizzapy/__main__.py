from .menu import MENU

""" Executable package
run in the outer dir, e.g.

    (cd ..; python -m pizzapy)
    

run in the outer of outer dir. e.g.

    (cd ../..; python -m src.pizzapy)

"""

print('Awesomeness of pizzas:')
for pizza in MENU:
    print(pizza.name, pizza.awesomeness())
