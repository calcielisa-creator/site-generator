import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    def test_parent_no_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])    
        self.assertRaises(ValueError, node.to_html)

    def test_parent_no_children(self):
        node = ParentNode("a", None )    
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_children(self):
        first_child_node = LeafNode("span", "first child")
        second_child_node = LeafNode("i", "second child")
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>first child</span><i>second child</i></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("a", "great-grandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><a>great-grandchild</a></b></span></div>",
        )
    
    def test_to_html_with_child_n_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"href": "...", "target": "..."})
        self.assertEqual(parent_node.to_html(), '<div href="..." target="..."><span>child</span></div>')
    