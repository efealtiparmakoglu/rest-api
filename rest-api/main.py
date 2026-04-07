#!/usr/bin/env python3
"""
{title}
A simple CLI tool I built to solve a specific problem
"""

import argparse
import os
import sys
from datetime import datetime

# Global config - might move to file later
CONFIG = {
    'version': '0.1.0',
    'author': 'Efe Altıparmakoğlu'
}

def process_file(filepath):
    """Process a single file"""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return False
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Main processing logic here
        result = len(content.split())
        print(f"Processed: {filepath}")
        print(f"Word count: {result}")
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='{title}')
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--version', action='version', version=f'%(prog)s {CONFIG["version"]}')
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Starting {title} v{CONFIG['version']}")
        print(f"Time: {datetime.now()}")
    
    if os.path.isfile(args.input):
        process_file(args.input)
    elif os.path.isdir(args.input):
        # Process all files in directory
        for filename in os.listdir(args.input):
            filepath = os.path.join(args.input, filename)
            if os.path.isfile(filepath):
                process_file(filepath)
    else:
        print(f"Error: {args.input} is not a valid file or directory")
        sys.exit(1)

if __name__ == '__main__':
    main()
