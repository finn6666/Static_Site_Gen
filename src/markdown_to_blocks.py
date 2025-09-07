def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Convert a markdown string into a list of block strings.
    Splits on double newlines and cleans up whitespace.

    Args:
        markdown (str): The input markdown text string.

    Returns:
        list[str]: A list of block strings representing paragraphs, headings, lists, etc.
    """
    # Split on double newlines to separate blocks
    blocks = markdown.split('\n\n')
    
    # Strip whitespace and filter out empty blocks
    cleaned_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:  # Only add non-empty blocks
            cleaned_blocks.append(stripped_block)
    
    return cleaned_blocks
