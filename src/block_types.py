import enum 
import re


class BlockType(enum.Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"  # Fixed typo
    ordered_list = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    """
    Determine the block type of a markdown block.
    
    Args:
        block (str): A single block of markdown text (whitespace already stripped)
    
    Returns:
        BlockType: The type of the block
    """
    lines = block.split('\n')
    
    # Check for heading (1-6 # characters, followed by space)
    if re.match(r'^#{1,6} ', block):
        return BlockType.heading
    
    # Check for code block (starts and ends with ```)
    if block.startswith('```') and block.endswith('```'):
        return BlockType.code
    
    # Check for quote block (every line starts with >)
    if all(line.startswith('>') for line in lines):
        return BlockType.quote
    
    # Check for unordered list (every line starts with -, *, or +, followed by space)
    if all(re.match(r'^[-*+] ', line) for line in lines):
        return BlockType.unordered_list
    
    # Check for ordered list (starts at 1, increments by 1, format: "number. ")
    if _is_ordered_list(lines):
        return BlockType.ordered_list
    
    # Default to paragraph
    return BlockType.paragraph


def _is_ordered_list(lines):
    """Helper function to validate ordered list format"""
    for i, line in enumerate(lines):
        expected_num = i + 1
        if not re.match(rf'^{expected_num}\. ', line):
            return False
    return True