# Static Site Generator Documentation

[< Back Home](/)

## Overview

This project is a custom static site generator built from scratch in Python. It converts Markdown content into a complete website with proper HTML structure, CSS styling, and navigation.

## Architecture

### Core Components

1. **Markdown Parser** - Handles textnode.py and htmlnode.py
   - Converts Markdown syntax to HTML nodes
   - Handles headings, paragraphs, lists, links, images, code blocks
   - Supports nested elements and complex formatting

2. **Page Generator** - Main generation logic  
   - Takes Markdown files and HTML templates
   - Generates complete HTML pages
   - Supports recursive directory processing

3. **Static Asset Manager** - File management
   - Copies CSS, images, and other static files
   - Maintains directory structure
   - Cleans destination before rebuilding

## Technical Features

### Markdown Support
- **Headers**: Hash symbols become HTML headings
- **Text Formatting**: Bold, italic, and code formatting
- **Links**: Bracket notation becomes anchor tags
- **Images**: Exclamation bracket notation becomes img tags
- **Lists**: Unordered and ordered lists
- **Blockquotes**: Greater than symbol becomes blockquote
- **Code Blocks**: Three backticks become pre code blocks

### Build System
- **Local Development**: Uses forward slash base path for localhost testing
- **Production Build**: Configurable base path for GitHub Pages deployment
- **Recursive Processing**: Automatically finds and converts all markdown files
- **Template System**: Single HTML template for consistent styling

## Usage

Run **python3 src/main.py** to build for local development.

Run **./build.sh** to build for GitHub Pages production.

Run **./main.sh** to start the development server.

## Project Structure

The main directories are:
- **src/** - Contains all Python source code
- **content/** - Contains all Markdown content files
- **static/** - Contains CSS, images, and other assets
- **docs/** - Contains the generated website files
- **template.html** - The HTML template used for all pages

## Build Process

1. **Clean**: Remove old generated files
2. **Copy Static**: Copy CSS, images, etc. to output directory
3. **Parse Markdown**: Convert all markdown files to HTML
4. **Apply Template**: Inject content into HTML template
5. **Fix Paths**: Adjust URLs for deployment environment
6. **Output**: Generate complete static website

## Deployment

### GitHub Pages Setup
1. Build site into docs directory
2. Push to GitHub repository
3. Enable Pages in repository settings
4. Set source to main branch, docs folder
5. Site automatically deploys to your GitHub Pages URL

### Path Configuration
- **Local**: Base path forward slash for development
- **Production**: Base path with repo name for GitHub Pages
- Automatically replaces href and src paths in generated HTML

## Key Learning Concepts

### Object-Oriented Design
- **TextNode**: Represents parsed Markdown elements
- **HTMLNode**: Builds HTML structure
- **Inheritance**: Different node types inherit from base classes

### File I/O and Path Handling
- Recursive directory traversal
- File reading and writing operations
- Cross-platform path handling

### Template Processing
- String replacement for dynamic content
- HTML template system
- Content injection

### Command Line Interface
- Command-line arguments for configuration
- Configurable build options
- Script automation

## Future Enhancements

### Potential Features
- **Live Reload**: Auto-refresh during development
- **Syntax Highlighting**: Code block highlighting
- **RSS Feed**: Auto-generate blog feed
- **Search**: Client-side search functionality
- **Themes**: Multiple template options
- **Plugin System**: Extensible architecture

### Performance Optimizations
- **Caching**: Skip unchanged files
- **Minification**: Compress CSS and HTML
- **Image Optimization**: Automatic image compression

## What I Learned

Building this static site generator taught me:

1. **Parsing Algorithms**: How to convert text formats to structured data
2. **Build Systems**: Understanding compilation and deployment pipelines
3. **Web Fundamentals**: HTML structure, CSS styling, and URL handling
4. **Python Proficiency**: File handling, OOP, and module organization
5. **DevOps Basics**: Deployment, version control, and automation

This project demonstrates end-to-end development skills from parsing algorithms to production deployment!
