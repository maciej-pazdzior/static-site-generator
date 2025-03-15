import unittest

from textnode import TextNode, TextType
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_node_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This `is` text `with` a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("code block", TextType.CODE),
                                        TextNode(" word", TextType.TEXT),
                                        TextNode("This ", TextType.TEXT),
                                        TextNode("is", TextType.CODE),
                                        TextNode(" text ", TextType.TEXT),
                                        TextNode("with", TextType.CODE),
                                        TextNode(" a ", TextType.TEXT),
                                        TextNode("code block", TextType.CODE),
                                        TextNode(" word", TextType.TEXT),
                                    ])
        
    def test_node_split_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        node2 = TextNode("This **is** text **with** a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                                        TextNode("This is text with a ", TextType.TEXT),
                                        TextNode("code block", TextType.BOLD),
                                        TextNode(" word", TextType.TEXT),
                                        TextNode("This ", TextType.TEXT),
                                        TextNode("is", TextType.BOLD),
                                        TextNode(" text ", TextType.TEXT),
                                        TextNode("with", TextType.BOLD),
                                        TextNode(" a ", TextType.TEXT),
                                        TextNode("code block", TextType.BOLD),
                                        TextNode(" word", TextType.TEXT),
                                    ])
        
    def test_split_images1(self):
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

    def test_split_images2(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images3(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). Some text and the end.",
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
                TextNode(". Some text and the end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images4(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). Some text and the end.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(". Some text and the end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images5(self):
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). Some text and the end.",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). Some text and the end.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(". Some text and the end.", TextType.TEXT),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(". Some text and the end.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()