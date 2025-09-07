# Static Site Generator

A custom static site generator built in Python that converts Markdown content to HTML using a configurable template system.

## Features

- **Markdown to HTML Conversion**: Supports headers, paragraphs, lists, links, images, code blocks, and blockquotes
- **Recursive Page Generation**: Automatically processes all markdown files in nested directories
- **Configurable Base Paths**: Support for both local development and GitHub Pages deployment
- **Template System**: Uses a single HTML template for consistent site styling

## Project Structure

```
├── src/                    # Source code
│   ├── main.py            # Main application entry point
│   ├── gen_page.py        # Page generation logic
│   ├── markdown_to_blocks.py  # Markdown parsing
│   ├── block_to_html.py   # HTML conversion
│   └── ...                # Supporting modules
├── content/               # Markdown content files
│   ├── index.md          # Main page
│   ├── blog/             # Blog posts
│   └── contact/          # Contact page
├── static/               # Static assets (CSS, images)
├── docs/                 # Generated site (for GitHub Pages)
├── template.html         # HTML template
├── build.sh             # Production build script
└── main.sh              # Development server script
```

## Usage

### Local Development
```bash
# Generate site for local development (base path: /)
python3 src/main.py

# Start development server
./main.sh
```

### Production Build
```bash
# Generate site for GitHub Pages (base path: /Static_Site_Gen/)
./build.sh
```

## Deployment

This site is configured for GitHub Pages deployment:

1. The production build generates files in the `docs/` directory
2. GitHub Pages serves from the `docs/` directory on the main branch
3. The live site is available at: https://finn6666.github.io/Static_Site_Gen/

## Development

The static site generator supports:
- Text formatting (bold, italic, code)
- Headers (H1-H6)
- Unordered and ordered lists
- Links and images
- Code blocks
- Blockquotes

All markdown files in the `content/` directory are automatically converted to HTML and placed in the appropriate location in the output directory.