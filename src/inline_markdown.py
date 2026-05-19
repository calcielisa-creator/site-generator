import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text)%2==0:
            raise Exception("Error: use of invalid markdown")

        for i, text in enumerate(split_text):
            if i%2 == 1:
                new_nodes.append(TextNode(text, text_type))
                continue
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images_tuple = extract_markdown_images(node.text)
        if images_tuple == []:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for image in images_tuple:
            delimiter = f"![{image[0]}]({image[1]})"
            split_text = remaining_text.split(delimiter, 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))    
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))    
            remaining_text =  split_text[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links_tuple = extract_markdown_links(node.text)
        if links_tuple == []:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for link in links_tuple:
            delimiter = f"[{link[0]}]({link[1]})"
            split_text = remaining_text.split(delimiter, 1)
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))    
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))    
            remaining_text =  split_text[1]

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    image_markdowns = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_markdowns

def extract_markdown_links(text):
    link_markdowns = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_markdowns