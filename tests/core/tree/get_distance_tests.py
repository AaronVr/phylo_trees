import unittest
from src.core.tree import *

class getDistanceTests(unittest.TestCase):
    def test_get_distance_one_vertex(self):
        parent = TreeNode()
        child = TreeNode(distance=10.0)
        parent.add_child(child)

        self.assertEqual(child.get_distance(parent), 10.0)
        self.assertEqual(parent.get_distance(child), 10.0)

    def test_get_distance_one_vertex_topology(self):
        parent = TreeNode()
        child = TreeNode(distance=10.0)
        parent.add_child(child)

        self.assertEqual(child.get_distance(parent, topology_only=True), 1.0)
        self.assertEqual(parent.get_distance(child, topology_only=True), 1.0)

    def test_get_distance_two_vertices(self):
        parent = TreeNode()
        left = TreeNode(distance=10.0)
        right = TreeNode(distance=5.0)
        parent.add_child(left)
        parent.add_child(right)

        self.assertEqual(left.get_distance(right), 15.0)
        self.assertEqual(right.get_distance(left), 15.0)

    def test_get_distance_two_vertices_topology(self):
        parent = TreeNode()
        left = TreeNode(distance=10.0)
        right = TreeNode(distance=5.0)
        parent.add_child(left)
        parent.add_child(right)

        self.assertEqual(left.get_distance(right, topology_only=True), 2.0)
        self.assertEqual(right.get_distance(left, topology_only=True), 2.0)