import re

from blocktype import BlockType

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        # Strip the entire block
        block = block.strip()
        # If it's not empty, process inner lines
        if block:
            # Split by newlines, strip each line, and rejoin
            lines = [line.strip() for line in block.split("\n")]
            cleaned_blocks.append("\n".join(lines))
    return cleaned_blocks

def block_to_block_type(block):
    if re.match("^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block[0] == ">":
        return BlockType.QUOTE
    elif block[:2] == "- ":
        return BlockType.UNORDERED_LIST
    elif block[:3] == "1. ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH