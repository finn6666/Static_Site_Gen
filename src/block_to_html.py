from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextNodeType
from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from text_to_nodes import text_to_nodes
import re


def markdown_to_html_node(markdown):
    """
    Convert markdown string to HTMLNode tree.
    
    Args:
        markdown (str): The markdown text to convert
        
    Returns:
        HTMLNode: A div containing all the block-level HTML elements
    """
    # Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Convert each block to HTMLNode
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        block_nodes.append(block_node)
    
    # Wrap all blocks in a div
    return ParentNode("div", block_nodes)


def block_to_html_node(block, block_type):
    """Convert a single block to its corresponding HTML node."""
    
    if block_type == BlockType.paragraph:
        # Replace newlines with spaces for paragraphs
        paragraph_text = block.replace('\n', ' ')
        children = text_to_children(paragraph_text)
        return ParentNode("p", children)
    
    elif block_type == BlockType.heading:
        # Extract heading level (count #'s)
        level = len(block.split(' ')[0])  # Count # characters
        heading_text = block[level + 1:]  # Remove "# " prefix
        children = text_to_children(heading_text)
        return ParentNode(f"h{level}", children)
    
    elif block_type == BlockType.code:
        # Remove ``` from start and end, don't parse inline markdown
        code_content = block[3:-3]  # Remove ``` from both ends
        # Only strip leading newlines, keep trailing newlines
        code_content = code_content.lstrip('\n')
        code_node = LeafNode("code", code_content)
        return ParentNode("pre", [code_node])
    
    elif block_type == BlockType.quote:
        # Remove > from each line
        lines = block.split('\n')
        quote_text = '\n'.join(line[1:].lstrip() for line in lines)  # Remove > and leading space
        children = text_to_children(quote_text)
        return ParentNode("blockquote", children)
    
    elif block_type == BlockType.unordered_list:
        # Create list items
        lines = block.split('\n')
        list_items = []
        for line in lines:
            # Remove list marker (-, *, or +) and space
            item_text = re.sub(r'^[-*+] ', '', line)
            item_children = text_to_children(item_text)
            list_items.append(ParentNode("li", item_children))
        return ParentNode("ul", list_items)
    
    elif block_type == BlockType.ordered_list:
        # Create list items
        lines = block.split('\n')
        list_items = []
        for line in lines:
            # Remove number, period, and space
            item_text = re.sub(r'^\d+\. ', '', line)
            item_children = text_to_children(item_text)
            list_items.append(ParentNode("li", item_children))
        return ParentNode("ol", list_items)
    
    else:
        raise ValueError(f"Unknown block type: {block_type}")


def text_to_children(text):
    """
    Convert text with inline markdown to list of HTMLNodes.
    
    Args:
        text (str): Text that may contain inline markdown
        
    Returns:
        list[HTMLNode]: List of HTML nodes representing the text
    """
    # Convert text to TextNodes using our existing function
    text_nodes = text_to_nodes(text)
    
    # Convert each TextNode to HTMLNode
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    
    return html_nodes


def text_node_to_html_node(text_node):
    """Convert a TextNode to an HTMLNode."""
    if text_node.node_type == TextNodeType.PLAIN:
        return LeafNode(None, text_node.text)
    elif text_node.node_type == TextNodeType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.node_type == TextNodeType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.node_type == TextNodeType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.node_type == TextNodeType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.node_type == TextNodeType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown TextNodeType: {text_node.node_type}")
