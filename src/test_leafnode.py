import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")    
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_leaf_with_props(self):
        node = LeafNode("a", "Hello, world!", {"href": "...", "target": "..."})
        self.assertEqual(node.to_html(), '<a href="..." target="...">Hello, world!</a>')  