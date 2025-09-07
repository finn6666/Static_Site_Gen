from textnode import TextNode, TextNodeType
from Extract_Links import extract_markdown_images, extract_markdown_links


def split_nodes_img(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # Only process TextNodes with PLAIN text type
        if not isinstance(node, TextNode) or node.node_type != TextNodeType.PLAIN:
            new_nodes.append(node)
            continue
        
        # Extract all images from this node's text
        images = extract_markdown_images(node.text)
        
        # If no images found, keep the original node
        if not images:
            new_nodes.append(node)
            continue
        
        # Split the text for each image found
        remaining_text = node.text
        
        for alt_text, url in images:
            # Reconstruct the full markdown syntax
            image_markdown = f"![{alt_text}]({url})"
            
            # Split the remaining text at this image (max 1 split)
            parts = remaining_text.split(image_markdown, 1)
            
            if len(parts) == 2:
                # Add text before the image (if not empty)
                before_text = parts[0]
                if before_text:
                    new_nodes.append(TextNode(before_text, TextNodeType.PLAIN))
                
                # Add the image node
                new_nodes.append(TextNode(alt_text, TextNodeType.IMAGE, url))
                
                # Continue with text after the image
                remaining_text = parts[1]
        
        # Add any remaining text after all images (if not empty)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextNodeType.PLAIN))
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        # Only process TextNodes with PLAIN text type
        if not isinstance(node, TextNode) or node.node_type != TextNodeType.PLAIN:
            new_nodes.append(node)
            continue
        
        # Extract all links from this node's text
        links = extract_markdown_links(node.text)
        
        # If no links found, keep the original node
        if not links:
            new_nodes.append(node)
            continue
        
        # Split the text for each link found
        remaining_text = node.text
        
        for anchor_text, url in links:
            # Reconstruct the full markdown syntax
            link_markdown = f"[{anchor_text}]({url})"
            
            # Split the remaining text at this link (max 1 split)
            parts = remaining_text.split(link_markdown, 1)
            
            if len(parts) == 2:
                # Add text before the link (if not empty)
                before_text = parts[0]
                if before_text:
                    new_nodes.append(TextNode(before_text, TextNodeType.PLAIN))
                
                # Add the link node
                new_nodes.append(TextNode(anchor_text, TextNodeType.LINK, url))
                
                # Continue with text after the link
                remaining_text = parts[1]
        
        # Add any remaining text after all links (if not empty)
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextNodeType.PLAIN))
    
    return new_nodes
