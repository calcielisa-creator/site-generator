import re

def extract_markdown_images(text):
    image_markdowns = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_markdowns

def extract_markdown_links(text):
    link_markdowns = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_markdowns