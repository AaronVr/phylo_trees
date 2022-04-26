import unittest
from src.core.tree import *

class IsLeafTests(unittest.TestCase):
    def test_is_leaf_single_node(self):
        node = TreeNode()

        self.assertTrue(node.is_leaf)

    def test_is_leaf_two_nodes(self):
        parent = TreeNode()
        child = TreeNode()
        parent.add_child(child)

        self.assertTrue(child.is_leaf)
        self.assertFalse(parent.is_leaf)
    
    def test_is_leaf_removed_child(self):
        parent = TreeNode()
        child = TreeNode()
        parent.add_child(child)
        parent.remove_child(child)
        
        self.assertTrue(parent.is_leaf)