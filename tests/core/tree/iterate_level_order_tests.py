import unittest
from src.core.tree import *

class IterateLevelOrderTests(unittest.TestCase):
    def test_iterate_level_order_small(self):
        """
           ┌─ 3
        1 ─┤
           └─ 2
        """
        root = TreeNode(name="1")
        left = TreeNode(name="2")
        right = TreeNode(name="3")
        root.add_child(left)
        root.add_child(right)

        iterator = root._iterate_levelorder()

        self.assertEqual(next(iterator), root)
        self.assertEqual(next(iterator), left)
        self.assertEqual(next(iterator), right)
    
