from textnode import TextNode, TextNodeType
from split_delim import split_nodes_delimiter
from split_img_and_links import split_nodes_img, split_nodes_link


def text_to_nodes(text: str) -> list[TextNode]:
    """
    Convert a markdown text string into a list of TextNode objects.
    Processes bold, italic, code, images, and links using the split functions.

    Args:
        text (str): The input markdown text string.

    Returns:
        list[TextNode]: A list of TextNode objects representing the parsed markdown.
    """
    # Start with a single plain text node
    nodes = [TextNode(text, TextNodeType.PLAIN)]
    
    # Process in order using our previously built functions:
    
    # 1. Split bold text (**text**)
    nodes = split_nodes_delimiter(nodes, "**", TextNodeType.BOLD)
    
    # 2. Split italic text (*text*)
    nodes = split_nodes_delimiter(nodes, "*", TextNodeType.ITALIC)
    
    # 3. Split italic text (_text_) - handle underscore syntax too
    nodes = split_nodes_delimiter(nodes, "_", TextNodeType.ITALIC)
    
    # 4. Split code text (`text`)
    nodes = split_nodes_delimiter(nodes, "`", TextNodeType.CODE)
    
    # 5. Split images ![alt](url)
    nodes = split_nodes_img(nodes)
    
    # 6. Split links [text](url)
    nodes = split_nodes_link(nodes)
    
    return nodes
