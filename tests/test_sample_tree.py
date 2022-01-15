"""
Test Tree
=========

Checks that your tree performs basic functionality.
"""

import unittest

from colours import Colours
from node import Node
from tree import Tree


class TestTree(unittest.TestCase):
    """
    Checks super basic tree functionality
    """

    def test_put(self):
        """
        Can we insert into tree?
        """

        root = Node(Colours.CYAN)

        t = Tree(root)

        a = Node(Colours.CYAN)

        t.put(root, a)

        assert len(root.children) == 1, \
            "[tree.put] should add child to node."

        assert root.children[0] == a, \
            "[tree.put] should add the correct node, yours did not."

        t.put(a, Node(Colours.YELLOW))

        assert len(root.children) == 1, \
            "[tree.put] should add child to node."

        assert root.children[0] == a, \
            "[tree.put] should add the correct node, yours did not."

        assert len(a.children) == 1, \
            "[tree.put] should add child to node."

    def test_put_propagate(self):
        """
        Does the colour propagate?
        """

        root = Node(Colours.CYAN)

        t = Tree(root)
        a = Node(Colours.BLUE)

        # Nothing should propagate yet
        assert Colours.CYAN.cmp(root.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        t.put(root, a)

        # It should now be blue!
        assert Colours.BLUE.cmp(root.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        t.put(a, Node(Colours.RED))

        # It should now be red!
        assert Colours.RED.cmp(root.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        assert Colours.RED.cmp(a.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

    def test_update_colour_propagates(self):
        """
        Does the colour propagate when changed?
        """

        root = Node(Colours.CYAN)

        t = Tree(root)
        a = Node(Colours.BLUE)

        t.put(root, a)
        t.put(a, Node(Colours.RED))

        # It should now be red!
        assert Colours.RED.cmp(root.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        assert Colours.RED.cmp(a.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        t.update_node_colour(a.children[0], Colours.NYAN)

        assert Colours.NYAN.cmp(root.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

        assert Colours.NYAN.cmp(a.propagated_colour) == 0, \
            "[propagate] Your colour didn't propagate correctly."

    def test_can_rm(self):
        """
        Can we remove a child?
        """

        root = Node(Colours.CYAN)

        t = Tree(root)

        a = Node(Colours.GREEN)
        b = Node(Colours.RED)

        t.put(root, a)
        t.put(root, b)

        assert len(root.children) == 2

        t.rm(b)

        assert len(root.children) == 1, \
            "[tree.rm] did not remove the node."

        assert b not in root.children, \
            "[tree.rm] did not remove the correct child."

    def test_rm_propagate(self):
        """
        Can we remove a child and the colour propagates?
        """

        root = Node(Colours.CYAN)

        t = Tree(root)

        a = Node(Colours.GREEN)
        b = Node(Colours.RED)

        t.put(root, a)
        t.put(root, b)

        assert Colours.RED.cmp(root.propagated_colour) == 0, \
            "Colour did not propagate with .put"

        assert Colours.GREEN.cmp(a.propagated_colour) == 0, \
            "Colour of sibling changed?"

        t.rm(b)

        assert Colours.GREEN.cmp(root.propagated_colour) == 0, \
            "Colour did not propagate when removing a child!"

    def test_can_swap_example(self):
        """
        Can you perform the swap in the comments?
        """

        A = Node(Colours.GREEN)

        B = Node(Colours.RED)
        C = Node(Colours.BLUE)

        D = Node(Colours.CYAN)
        J = Node(Colours.CYAN)
        K = Node(Colours.YELLOW)

        t = Tree(A)

        t.put(A, B)
        t.put(A, C)
        t.put(B, D)
        t.put(C, J)
        t.put(C, K)

        # Let's swap
        t.swap(D, C)

        # Let's check if it worked!
        assert D.parent == A, \
            "[tree.swap] Did not change parent."

        assert C.parent == B, \
            "[tree.swap] Did not change parent."

        assert D not in B.children, \
            "[tree.swap] Did not remove child from old parent."

        assert C not in A.children, \
            "[tree.swap] Did not remove child from old parent."

        assert C in B.children, \
            "[tree.swap] child incorrectly swapped to children list."

        assert D in A.children, \
            "[tree.swap] child incorrectly swapped to children list."

    def test_depth_example(self):
        """
        Can you perform the is_coloured function?


        (start)---> G
                   / \
              (A) G   G (B)
                 /|    \
           (A1) G R(A2) G (B1)
                  |
                  R (A21)
        """

        root = Node(Colours.GREEN)

        A = Node(Colours.GREEN)
        B = Node(Colours.GREEN)

        A1 = Node(Colours.GREEN)
        A2 = Node(Colours.RED)
        A21 = Node(Colours.RED)

        B1 = Node(Colours.GREEN)

        t = Tree(root)

        t.put(root, A)
        t.put(root, B)

        t.put(A, A1)
        t.put(A, A2)
        t.put(A2, A21)
        t.put(B, B1)

        assert t.is_coloured_to_depth_k(root, Colours.GREEN, 0), \
            "[is_coloured] Returned false, should be true!"

        assert not t.is_coloured_to_depth_k(root, Colours.RED, 0), \
            "[is_coloured] Returned true, should be false!"

        assert not t.is_coloured_to_depth_k(root, Colours.GREEN, 2), \
            "[is_coloured] Returned true, should be false!"

        assert t.is_coloured_to_depth_k(root, Colours.GREEN, 1), \
            "[is_coloured] Returned false, should be true!"
