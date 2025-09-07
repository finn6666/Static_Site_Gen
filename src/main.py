import os
import shutil
import sys
from textnode import TextNode, TextNodeType  # Remove 'src.'
from gen_page import generate_page, generate_pages_recursively  # Remove 'src.'

def copy_static_to_public(src_dir="static", dest_dir="docs"):
    """
    Recursively copy all contents from source directory to destination directory.
    Clears destination first to ensure clean copy.
    """
    print(f"Starting copy from {src_dir} to {dest_dir}")
    
    # Clear destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Cleared destination directory: {dest_dir}")
    
    # Create fresh destination directory
    os.makedirs(dest_dir)
    print(f"Created destination directory: {dest_dir}")
    
    # Copy contents recursively
    copy_directory_contents(src_dir, dest_dir)
    print("Copy complete!")

def copy_directory_contents(src_dir, dest_dir):
    """Helper function to recursively copy directory contents."""
    # Get all items in source directory
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(src_path):
            # Copy file
            shutil.copy2(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            # Create directory and recurse
            os.makedirs(dest_path)
            print(f"Created directory: {dest_path}")
            copy_directory_contents(src_path, dest_path)  # Recursive call

def main():
    print("=== Starting Static Site Generation ===")
    
    # Get base path from command line arguments, default to "/"
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    print(f"Using base path: {base_path}")
    
    # 1. Delete anything in docs directory and copy static files
    copy_static_to_public()
    
    # 2. Generate HTML pages for all markdown files in content directory
    print("\n=== Generating HTML pages recursively ===")
    generate_pages_recursively(
        dir_path_content="content",
        template_path="template.html", 
        dest_dir_path="docs",
        base_path=base_path
    )
    
    print("\n=== Site generation complete! ===")

if __name__ == "__main__":
    main()

