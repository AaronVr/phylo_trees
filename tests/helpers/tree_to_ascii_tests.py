import unittest
from src.helpers import *
from src.core.tree import *


class TreeToAsciiTests(unittest.TestCase):
    def test_tree_to_ascii(self):
        test = """ ┌─ 2 
 │ 
─┼─ 3 
 │ 
 └─ 4 """
        tree = TreeNode(name="1")
        child1 = TreeNode(name="2")
        child2 = TreeNode(name="3")
        child3 = TreeNode(name="4")
        tree.add_child(child1)
        tree.add_child(child2)
        tree.add_child(child3)

        self.assertEqual(tree.__str__(), test)