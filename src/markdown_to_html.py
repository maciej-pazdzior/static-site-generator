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
            BlockType.HEADING: 'h1',
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
            block = block.replace("\n", " ")
            parent_node = ParentNode(tags[block_type], text_to_children(block, block_type))
            html_blocks.append(parent_node)
    div_parent = ParentNode("div", html_blocks)
    return div_parent

def text_to_children(text, block_type):
    if block_type == BlockType.UNORDERED_LIST:
        list_items = text.split("- ")
        html_nodes = []
        for item in list_items:
            if item:
                item = item.strip()
                html_nodes.append(LeafNode("li", item))
    else:
        text_nodes = text_to_textnodes(text)
        html_nodes = list(map(lambda node: text_node_to_html_node(node), text_nodes))
    return html_nodes