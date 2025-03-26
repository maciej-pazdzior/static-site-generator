import sys

from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from page_generator import generate_page, generate_pages_recursive

def main():
    copy_static_to_public()
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    generate_pages_recursive("content/", "template.html", "docs/", basepath)
         
if __name__ == "__main__":
    main()