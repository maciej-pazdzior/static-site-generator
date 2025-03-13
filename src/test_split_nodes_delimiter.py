import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

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

if __name__ == "__main__":
    unittest.main()