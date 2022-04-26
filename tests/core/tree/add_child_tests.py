import unittest
from src.core.tree import *

class addChildTests(unittest.TestCase):
    def test_add_1_child(self):
        parent = TreeNode()
        child = TreeNode()
        parent.add_child(child)

        self.assertEqual(parent.children[0], child)

    def test_add_2_children(self):
        parent = TreeNode()
        child1 = TreeNode()
        child2 = TreeNode()
        parent.add_child(child1)
        parent.add_child(child2)

        self.assertEqual(parent.children[0], child1)
        self.assertEqual(parent.children[1], child2)

    def test_add_100_children(self):
        parent = TreeNode()
        for i in range(0, 100):
            child = TreeNode()
            parent.add_child(child)

            self.assertEqual(parent.children[i], child)

    def test_add_sets_parent(self):
        parent = TreeNode()
        child = TreeNode()
        parent.add_child(child)

        self.assertEqual(child.parent, parent)
