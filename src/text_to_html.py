from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    match text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, text_node.url)
        case TextType.IMAGE:
            return LeafNode("img", "", text_type.url, text_type.alt)
        case _:
            raise Exception("Wrong type")