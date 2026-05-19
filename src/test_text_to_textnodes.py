import unittest

from textnode import TextType, TextNode
from inline_markdown import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_tn(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
    
    def test_text_to_tn_another_order(self):
        text = "This is text with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and an _italic_ word and a `code block` and a [link](https://boot.dev)"

        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_text_to_tn_no_texttypes(self):

        text = "This is text with no italic, no code block and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, [
            TextNode("This is text with no italic, no code block and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
    
    def test_text_to_tn_no_image_no_link(self):
        text = "This is **text** with an _italic_ word and a `code block` and no images or links"
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and no images or links", TextType.TEXT),
            ]
        )

    def test_text_to_tn_no_text(self):
        text = ""
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, [])
