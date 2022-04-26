import unittest
from src.core.tree import *

class getDistanceTests(unittest.TestCase):
    def test_get_distance_one_vertex(self):
        parent = TreeNode()
        child = TreeNode(distance=10.0)
        parent.add_child(child)

        self.assertEqual(child.get_distance(parent), 10.0)
        self.assertEqual(parent.get_distance(child), 10.0)