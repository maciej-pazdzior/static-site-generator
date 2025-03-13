from textnode import TextNode, TextType

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