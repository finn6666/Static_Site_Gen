#!/bin/bash

echo "Generating static site..."
python3 src/main.py

# Check if site generation was successful
if [ $? -eq 0 ]; then
    echo "Site generation complete!"
    echo "Starting web server on http://localhost:8888"
    echo "Press Ctrl+C to stop the server"
    
    # Start the web server in the public directory
    cd public && python3 -m http.server 8888
else
    echo "Site generation failed!"
    exit 1
fi
