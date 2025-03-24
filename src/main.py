from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from page_generator import generate_page

def main():
    copy_static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")
         
if __name__ == "__main__":
    main()