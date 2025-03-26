import re
import os

from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    html = markdown_to_html_node(markdown).to_html()
    title = re.search(r"<h1>(.+?)</h1>", html).group(1)
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        md_content = f.read()
    with open(template_path) as f:
        template_content = f.read()
    html_string = markdown_to_html_node(md_content).to_html()
    page_title = extract_title(md_content)
    template_content = template_content.replace("{{ Title }}", page_title)
    template_content = template_content.replace("{{ Content }}", html_string)
    with open(dest_path, "x") as f:
        f.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    objects = os.listdir(dir_path_content)
    for object in objects:
        object_path = os.path.join(dir_path_content, object)
        if os.path.isfile(object_path):
            new_file_path = os.path.join(dest_dir_path, object)
            new_file_path = new_file_path.replace("md", "html")
            generate_page(object_path, template_path, new_file_path)
        else:
            new_dir_path = os.path.join(dest_dir_path, object)
            os.mkdir(new_dir_path)
            generate_pages_recursive(object_path, template_path, new_dir_path)
