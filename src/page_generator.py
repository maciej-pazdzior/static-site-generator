import re

from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    html = markdown_to_html_node(markdown).to_html()
    title = re.search(r"<h1>(.+?)</h1>", html).group(1)
    return title