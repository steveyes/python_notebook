from dataclasses import dataclass, field


@dataclass
class CC2:
    a: float
    b: float
    c: float = field(init=False, repr=True)

    """The generated __init__() code will call a method named __post_init__(), if __post_init__() is defined on the 
    class. It will normally be called as self.__post_init__(). However, if any InitVar fields are defined, 
    they will also be passed to __post_init__() in the order they were defined in the class. If no __init__() method 
    is generated, then __post_init__() will not automatically be called. """

    def __post_init__(self):
        self.c = self.a + self.b


c = CC2(1, 2)

print(c)
