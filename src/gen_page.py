from block_to_html import markdown_to_html_node  # Remove 'src.'


def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No level-1 heading found")


def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as mkdown_file:
        markdown_content = mkdown_file.read()
    
    # Read the template file
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    # Convert markdown to HTML using our function
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title from markdown
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    # Replace base path references
    final_html = final_html.replace('href="/', f'href="{base_path}')
    final_html = final_html.replace('src="/', f'src="{base_path}')
    
    # Write the final HTML to destination
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)
    
    print(f"Page generated successfully!")

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, base_path="/"):
    """
    Recursively generate HTML pages from all markdown files in content directory.
    
    Args:
        dir_path_content: Path to the content directory containing markdown files
        template_path: Path to the HTML template file
        dest_dir_path: Path to the destination directory for generated HTML files
        base_path: Base path for URLs in the generated HTML
    """
    import os
    
    print(f"Crawling directory: {dir_path_content}")
    
    # Ensure destination directory exists
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    # Get all items in the content directory
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(src_path):
            # Check if it's a markdown file
            if item.endswith('.md'):
                # Generate HTML filename (replace .md with .html)
                html_filename = item.replace('.md', '.html')
                dest_path = os.path.join(dest_dir_path, html_filename)
                
                # Generate the page
                generate_page(src_path, template_path, dest_path, base_path)
                
        elif os.path.isdir(src_path):
            # Create corresponding directory in destination
            dest_subdir = os.path.join(dest_dir_path, item)
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            
            # Recursively process subdirectory
            generate_pages_recursively(src_path, template_path, dest_subdir, base_path)