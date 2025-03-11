import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        returned = HTMLNode("p", "sample text", None, {
                    "href": "https://www.google.com",
                    "target": "_blank",
                    }).props_to_html()
        expect = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(returned, expect)


if __name__ == "__main__":
    unittest.main()