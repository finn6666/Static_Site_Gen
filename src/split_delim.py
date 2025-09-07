from textnode import TextNode, TextNodeType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split TextNodes on a delimiter, alternating between PLAIN and the specified text_type.
    
    Args:
        old_nodes: List of TextNode objects
        delimiter: String delimiter to split on (e.g., "**", "*", "`")
        text_type: TextNodeType to use for delimited text
    
    Returns:
        List of TextNode objects with delimited text split into separate nodes
    """
    new_nodes = []
    
    for node in old_nodes:
        # Only process TextNodes with PLAIN text type
        if not isinstance(node, TextNode) or node.node_type != TextNodeType.PLAIN:
            new_nodes.append(node)
            continue
        
        # Split the text on the delimiter
        parts = node.text.split(delimiter)
        
        # Check for unmatched delimiters (odd number of parts means unmatched)
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched {delimiter} delimiter in text: {node.text}")
        
        # Process each part, alternating between PLAIN and the specified type
        for i, part in enumerate(parts):
            if part:  # Only add non-empty parts
                if i % 2 == 0:
                    # Even indices are plain text
                    new_nodes.append(TextNode(part, TextNodeType.PLAIN))
                else:
                    # Odd indices are delimited text
                    new_nodes.append(TextNode(part, text_type))
    
    return new_nodes
