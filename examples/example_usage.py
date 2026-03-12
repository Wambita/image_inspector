#!/usr/bin/env python3
"""
Example usage of Image Inspector modules
"""

import sys
sys.path.insert(0, '../src')

from modules.metadata_extractor import extract_metadata
from modules.steganography_detector import detect_steganography

def analyze_image(image_path):
    """Analyze an image for both metadata and steganography"""
    print(f"Analyzing: {image_path}\n")
    
    print("=== METADATA ===")
    metadata = extract_metadata(image_path)
    print(metadata)
    
    print("\n=== STEGANOGRAPHY ===")
    hidden_data = detect_steganography(image_path)
    print(hidden_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 example_usage.py <image_path>")
        sys.exit(1)
    
    analyze_image(sys.argv[1])
