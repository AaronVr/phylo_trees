import unittest
from src.parsers.newick_parser import parse_newick_tree

class ParseNewickTests(unittest.TestCase):
    def test_parse_simple_newick_format0(self):
        tree_string = "(,);"
        tree = parse_newick_tree(tree_string)

        self.assertEqual(len(tree.children), 2)

    def test_parse_complex_newick_format0(self):
        tree_string = "(,(,,),);"
        tree = parse_newick_tree(tree_string)

        self.assertEqual(len(tree.children), 3)
        self.assertEqual(len(tree.children[0]), 1)
        self.assertEqual(len(tree.children[0].children), 0)

        self.assertEqual(len(tree.children[1]), 3)
        self.assertEqual(len(tree.children[1].children[0].children), 0)
        self.assertEqual(len(tree.children[1].children[1].children), 0)
        self.assertEqual(len(tree.children[1].children[2].children), 0)

        self.assertEqual(len(tree.children[2]), 1)
        self.assertEqual(len(tree.children[2].children), 0)

    def test_parse_whitespace_newick_format0(self):
        tree_string = "( , ( , , ) , );"
        tree = parse_newick_tree(tree_string)

        self.assertEqual(len(tree.children), 3)
        self.assertEqual(len(tree.children[0]), 1)
        self.assertEqual(len(tree.children[0].children), 0)

        self.assertEqual(len(tree.children[1]), 3)
        self.assertEqual(len(tree.children[1].children[0].children), 0)
        self.assertEqual(len(tree.children[1].children[1].children), 0)
        self.assertEqual(len(tree.children[1].children[2].children), 0)

        self.assertEqual(len(tree.children[2]), 1)
        self.assertEqual(len(tree.children[2].children), 0)