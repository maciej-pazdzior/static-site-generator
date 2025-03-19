import unittest

from blocks_markdown import markdown_to_blocks, block_to_block_type
from blocktype import BlockType

class TestBlocksMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        blocks = [
            "###### Heading 1",
            "``` Some code ```",
            "> First quote\n> Second quote",
            "- This is a list\n- with items",
            "1. First item\n2. Second item",
            "Normal paragraph"
        ]
        block_types = list(map(lambda block: block_to_block_type(block), blocks))
        self.assertEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH
            ]
        )


if __name__ == "__main__":
    unittest.main()