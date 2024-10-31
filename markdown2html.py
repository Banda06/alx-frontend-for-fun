#!/usr/bin/python3
"""
markdown2html.py - Converts a Markdown file to an HTML file

Usage:
    ./markdown2html.py <input_markdown_file> <output_html_file>

Requirements:
    - Takes two arguments: input Markdown file and output HTML file.
    - If the number of arguments is less than 2, print an error message and exit with status 1.
    - If the input Markdown file does not exist, print an error message and exit with status 1.
    - If successful, generate the output file and exit with status 0.
"""

import sys
import os
import re

def markdown_to_html(markdown_text):
    """
    Converts Markdown text to HTML.
    
    Supports:
    - Heading levels 1 to 6
    - Bold and italic formatting
    """
    html = markdown_text

    # Parse heading levels from 1 to 6
    for i in range(6, 0, -1):  # Start from level 6 to level 1
        pattern = r'^' + ('#' * i) + r' (.+)$'
        replacement = f'<h{i}>\\1</h{i}>'
        html = re.sub(pattern, replacement, html, flags=re.MULTILINE)

    # Convert bold (**) and italic (*) syntax
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    return html

def main():
    # Check for the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Assign input and output file arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the input Markdown file
    with open(input_file, 'r') as markdown_file:
        markdown_text = markdown_file.read()

    # Convert Markdown to HTML
    html_text = markdown_to_html(markdown_text)

    # Write the converted HTML to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_text)

    # Exit successfully
    sys.exit(0)

if __name__ == "__main__":
    main()
