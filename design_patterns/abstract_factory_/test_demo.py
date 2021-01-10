#!/usr/bin/env python3
#

class World(object):
    def make_character(self):
        return Hero()

    def make_obstacle(self):
        return Badass()


class Hero(object):
    def __init__(self, name=None):
        self.name = name

    def interact_with(self, obstacle):
        pass


class Badass(object):
    def action(self):
        pass


class Frog(Hero):

    def __init__(self, name=None):
        super().__init__(name)

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle):
        print(f'''{self} the Frog encounters {obstacle} and {obstacle.action()}''')


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return "eats it"


class FrogWorld(World):
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\nWelcome to {'-'*10}Frog World{'-'*10}"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(Hero):

    def __init__(self, name=None):
        super().__init__(name)

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f'''{self} the Wizard battles against {obstacle} and {obstacle.action()}''')


class ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld(World):
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\nWelcome to {'-'*10}Wizard World{'-'*10}"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return ork()


class GameEnviroment:
    def __init__(self, factory: World):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f"Welcome {name}. How old are you?\n")
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...\n")
        return (False, age)
    return (True, age)


if __name__ == '__main__':
    name = input("Hello, What's your name?\n")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if int(age) < 18 else WizardWorld
    environment = GameEnviroment(game(name))
    environment.play()
