import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    def test_props_empty(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), "")
    def test_props_format(self):
        node = HTMLNode(None, None, None, {"href": "...", "target": "..."})
        self.assertEqual(node.props_to_html(), f' href="..." target="..."')