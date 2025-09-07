# Static Site Generator Documentation

[< Back Home](/)

## Overview

This project is a **custom static site generator** built from scratch in Python. It converts Markdown content into a complete website with proper HTML structure, CSS styling, and navigation.

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
- **Headers**: `# ## ###` becomes `<h1> <h2> <h3>`
- **Text Formatting**: Bold, italic, and code formatting
- **Links**: `[text](url)` becomes `<a href="url">text</a>`
- **Images**: `![alt](src)` becomes `<img src="src" alt="alt">`
- **Lists**: Unordered and ordered lists
- **Blockquotes**: `>` becomes `<blockquote>`
- **Code Blocks**: Three backticks become `<pre><code>`

### Build System
- **Local Development**: Uses `/` base path for localhost testing
- **Production Build**: Configurable base path for GitHub Pages deployment
- **Recursive Processing**: Automatically finds and converts all `.md` files
- **Template System**: Single HTML template for consistent styling

## Usage

### Local Development
```bash
python3 src/main.py
# Builds site with base path "/" into docs/ directory
```

### Production Build
```bash
./build.sh
# Builds site with base path "/Static_Site_Gen/" for GitHub Pages
```

### Development Server
```bash
./main.sh
# Starts local server at http://localhost:8888
```

## Project Structure

```
Static-Site-Gen/
├── src/                    # Source code
│   ├── main.py            # Main build script
│   ├── gen-page.py        # Page generation logic
│   ├── textnode.py        # Markdown parsing
│   └── htmlnode.py        # HTML node classes
├── content/               # Markdown content
│   ├── index.md          # Homepage
│   ├── blog/             # Blog posts
│   └── contact/          # Contact page
├── static/               # Static assets
│   ├── index.css         # Styles
│   └── images/           # Images
├── docs/                 # Generated site (GitHub Pages)
├── template.html         # HTML template
└── build.sh              # Production build script
```

## Build Process

1. **Clean**: Remove old generated files
2. **Copy Static**: Copy CSS, images, etc. to output directory
3. **Parse Markdown**: Convert all `.md` files to HTML
4. **Apply Template**: Inject content into HTML template
5. **Fix Paths**: Adjust URLs for deployment environment
6. **Output**: Generate complete static website

## Deployment

### GitHub Pages Setup
1. Build site into docs/ directory
2. Push to GitHub repository
3. Enable Pages in repository settings
4. Set source to main branch, docs/ folder
5. Site automatically deploys to your GitHub Pages URL

### Path Configuration
- **Local**: Base path "/" for development
- **Production**: Base path "/Static-Site-Gen/" for GitHub Pages
- Automatically replaces href="/" and src="/" in generated HTML

## Key Learning Concepts

### Object-Oriented Design
- **TextNode**: Represents parsed Markdown elements
- **HTMLNode**: Builds HTML structure
- **Inheritance**: Different node types inherit from base classes

### File I/O and Path Handling
- Recursive directory traversal
- File reading/writing operations
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
- **Minification**: Compress CSS/HTML
- **Image Optimization**: Automatic image compression

## What I Learned

Building this static site generator taught me:

1. **Parsing Algorithms**: How to convert text formats to structured data
2. **Build Systems**: Understanding compilation and deployment pipelines
3. **Web Fundamentals**: HTML structure, CSS styling, and URL handling
4. **Python Proficiency**: File handling, OOP, and module organization
5. **DevOps Basics**: Deployment, version control, and automation

This project demonstrates end-to-end development skills from parsing algorithms to production deployment!
