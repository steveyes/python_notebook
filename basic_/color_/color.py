from colorama import Fore
from colorama import Style

class Color:
    def __init__(self) -> None:
        super().__init__()
        self.msg = str("None color given and None message given")

    def __coloring(self, _color, _msg):
        self.msg = f"{_color}{_msg}{Style.RESET_ALL}"
        return self

    def red(self, msg: str):
        return self.__coloring(Fore.RED, msg)

    def green(self, msg: str):
        return self.__coloring(Fore.GREEN, msg)

    def blue(self, msg: str):
        return self.__coloring(Fore.BLUE, msg)

    def print(self):
        print(self)

    def __str__(self):
        return self.msg
