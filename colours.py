"""
Defines the colours we will be using in the assignment.

*** DO NOT MODIFY ***
"""

import sys


class Colour:
    """
    Colour class defines the colours we will be using in the assignment.
    """

    def __init__(self, name: str) -> None:
        self.NAME = name

    def cmp(self, Y: 'Colour') -> int:
        # Colour heirarchy
        # NYAN is the best... of course

        si = -1
        sy = -1

        try:
            si = Colours._HEIRARCHY.index(self)
        except ValueError:
            print("Apparently I'm not a colour.. I should not exist.")
            sys.exit(1)

        try:
            sy = Colours._HEIRARCHY.index(Y)
        except ValueError:
            print(f"Failed to compare Colour: {Y}")
            sys.exit(1)

        if si > sy:
            return -1
        elif si < sy:
            return 1
        else:
            return 0


class Colours:
    """
    Colours class defines all the colours.
    """

    RED = Colour("R")
    GREEN = Colour("G")
    BLUE = Colour("B")
    CYAN = Colour("C")
    YELLOW = Colour("Y")
    NYAN = Colour("CAT")

    _HEIRARCHY = [
        NYAN,
        RED,
        GREEN,
        BLUE,
        CYAN,
        YELLOW,
    ]
