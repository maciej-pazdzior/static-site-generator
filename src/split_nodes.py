from textnode import TextNode, TextType
from extract_images_and_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        try:
            node_splitted = node.text.split(delimiter)
        except:
            raise Exception("Invalid Markdown syntax")
        nodes_list = []
        for node in node_splitted:
            if node_splitted.index(node) % 2 == 0:
                nodes_list.append(TextNode(node, TextType.TEXT))
            else:
                nodes_list.append(TextNode(node, text_type))
        new_nodes.extend(nodes_list)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        images = extract_markdown_images(original_text)
        nodes_list = []
        for image in images:
            link_alt = image[0]
            link_url = image[1]
            sections = original_text.split(f"![{link_alt}]({link_url})", 1)
            if sections[0]:
                nodes_list.append(TextNode(sections[0], TextType.TEXT))
            nodes_list.append(TextNode(link_alt, TextType.IMAGE, link_url))
            original_text = sections[1]
        if original_text:
            nodes_list.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(nodes_list)
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_links(original_text)
        nodes_list = []
        for link in links:
            link_alt = link[0]
            link_url = link[1]
            sections = original_text.split(f"[{link_alt}]({link_url})", 1)
            if sections[0]:
                nodes_list.append(TextNode(sections[0], TextType.TEXT))
            nodes_list.append(TextNode(link_alt, TextType.LINK, link_url))
            original_text = sections[1]
        if original_text:
            nodes_list.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(nodes_list)
    return new_nodes
