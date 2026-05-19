import unittest

from textnode import TextType, TextNode
from split_nodes_funcs import split_nodes_image, split_nodes_link

class TestSplitNodesImageAndLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://fake-site.com/3elNhQu.bla)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://fake-site.com/3elNhQu.bla"
                ),
            ],
            new_nodes,
        )
    

    def test_split_link_image(self):
        node = TextNode(
            "This is text with a [link](https://fake-site.com/3elNhQu.bla) and an ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes_images = split_nodes_image([node])
        new_nodes_links = split_nodes_link([node])


        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://fake-site.com/3elNhQu.bla"),
                TextNode(" and an ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes_links,
        )

        self.assertListEqual(
            [
                TextNode("This is text with a [link](https://fake-site.com/3elNhQu.bla) and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes_images,
        )

    def test_no_split(self):
        node = TextNode(
            "This is text with nothing in it",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with nothing in it", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_more_nodes(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is another text with an ![image](https://i.imgur.com/dfuwhdef.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is another text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/dfuwhdef.png"),
            ],
            new_nodes,
        )
    
