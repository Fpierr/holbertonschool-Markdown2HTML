#!/usr/bin/python3
"""
Module to convert Markdown to HTML
"""

import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]  # Placeholder for future use.

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Placeholder for future Markdown to HTML conversion logic.
    sys.exit(0)

if __name__ == "__main__":
    main()
