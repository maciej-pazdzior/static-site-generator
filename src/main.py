from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from page_generator import generate_page, generate_pages_recursive

def main():
    copy_static_to_public()
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content/", "template.html", "public/")
         
if __name__ == "__main__":
    main()