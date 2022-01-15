"""
Test Node
=========

Tests that the node has basic functionality.
You will need to ensure that you cover more tests.
"""

import unittest

from node import Node
from colours import Colours


class TestNodeFunc(unittest.TestCase):
    """
    Check basic node functionality
    """

    def test_can_set_colour(self):
        """
        Can we change colour?
        """

        nod = Node(Colours.GREEN)

        assert Colours.GREEN.cmp(nod.colour) == 0, \
            "Your colour wasn't set properly in constructor"

        nod.update_colour(Colours.YELLOW)

        assert Colours.YELLOW.cmp(nod.colour) == 0, \
            "[node.update_colour] Your colour was not updated."

    def test_can_add_child(self):
        """
        Can we add a child?
        """

        ash = Node(Colours.GREEN)

        pikachu = Node(Colours.YELLOW)
        charmander = Node(Colours.RED)
        squirtle = Node(Colours.BLUE)
        bulbasaur = Node(Colours.GREEN)

        ash.add_child(pikachu)

        assert pikachu in ash.children, \
            "Node was not added to children."

        ash.add_child(charmander)
        ash.add_child(squirtle)
        ash.add_child(bulbasaur)

        assert len(ash.children) == 4, \
            "Node did not add all the children."

        for sel in [charmander, squirtle, bulbasaur, pikachu]:
            assert sel in ash.children, \
                "Node did not get added to children."

    def test_can_remove_child(self):
        """
        Can we remove a child?
        """

        """
        Can we add a child?
        """

        ash = Node(Colours.GREEN)

        pikachu = Node(Colours.YELLOW)
        charmander = Node(Colours.RED)
        squirtle = Node(Colours.BLUE)
        bulbasaur = Node(Colours.GREEN)

        ash.add_child(pikachu)
        ash.add_child(charmander)
        ash.add_child(squirtle)
        ash.add_child(bulbasaur)

        assert len(ash.children) == 4, \
            "Node did not add all the children."

        ash.remove_child(squirtle)

        assert len(ash.children) == 3, \
            "Node did not remove the child."
