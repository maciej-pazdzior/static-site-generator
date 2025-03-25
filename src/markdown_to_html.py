import re

from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from blocktype import BlockType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        tags = {
            BlockType.PARAGRAPH: "p",
            BlockType.HEADING: 'h',
            BlockType.CODE : "code",
            BlockType.QUOTE: "blockquote",
            BlockType.UNORDERED_LIST: "ul",
            BlockType.ORDERED_LIST: "ol"
        }
        if  block_type == BlockType.CODE:
            block = block[4:-3]
            text_node = TextNode(block, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            pre_parent = ParentNode("pre", [html_node])
            html_blocks.append(pre_parent)

        else:
            if block_type == BlockType.QUOTE:
                block = block[2:]
                block = block.replace(">", " ")
            block = block.replace("\n", " ")
            if block_type == BlockType.HEADING:
                heading_hashes = re.match("^#{1,6}", block).group(0)
                hash_count = len(heading_hashes)
                tag = f"h{hash_count}"
                block = block[hash_count+1:]
                parent_node = ParentNode(tag, text_to_children(block, block_type))
            else:
                parent_node = ParentNode(tags[block_type], text_to_children(block, block_type))
            html_blocks.append(parent_node)
    div_parent = ParentNode("div", html_blocks)
    return div_parent

def text_to_children(text, block_type=None):
    if block_type == BlockType.UNORDERED_LIST:
        list_items = text.split("- ")
        html_nodes = []
        for item in list_items:
            if item:
                item = item.strip()
                html_nodes.append(ParentNode("li", text_to_children(item)))
    elif block_type == BlockType.ORDERED_LIST:
        list_items = re.split(r"\d+\.", text)
        html_nodes = []
        for item in list_items:
            if item:
                item = item.strip()
                html_nodes.append(ParentNode("li", text_to_children(item)))
    else:
        text_nodes = text_to_textnodes(text)
        html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return html_nodes