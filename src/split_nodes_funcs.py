from textnode import TextNode, TextType
from extract_markdown_funcs import extract_markdown_images, extract_markdown_links

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