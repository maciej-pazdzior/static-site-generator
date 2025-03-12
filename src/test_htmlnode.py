import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        returned = HTMLNode("p", "sample text", None, {
                    "href": "https://www.google.com",
                    "target": "_blank",
                    }).props_to_html()
        expect = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(returned, expect)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()