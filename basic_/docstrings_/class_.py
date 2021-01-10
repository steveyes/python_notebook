from pydoc import render_doc
from typing import Optional


class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        # reStructured Text Example
        """
        :param name: The name of the animal
        :param sound: The sound the animal makes
        :param num_legs: The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound: Optional[str] = None):
        # NumPy/SciPy Docstrings Example
        """Print what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal sound is used.

        Parameters
        ----------
        sound : Optional[str]
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))


print(render_doc(Animal))
# print(Animal.__doc__)
