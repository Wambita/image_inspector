#!/usr/bin/env python3
import sys
import argparse
from modules.metadata_extractor import extract_metadata
from modules.steganography_detector import detect_steganography

def main():
    parser = argparse.ArgumentParser(
        description="Welcome to Image Inspector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
OPTIONS:
    -m  Metadata          Extract metadata from the image (e.g., geolocation, device info)
    -s  Steganography     Detect and extract hidden data from the image using steganography techniques
    -o  "FileName"        Specify the file name to save output
    --help                Display this help message
        """
    )
    
    parser.add_argument('-m', '--metadata', action='store_true', help='Extract metadata')
    parser.add_argument('-s', '--steganography', action='store_true', help='Detect steganography')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('image', help='Image file to analyze')
    
    if len(sys.argv) == 1 or '--help' in sys.argv:
        print("Welcome to Image Inspector\n")
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    result = ""
    
    if args.metadata:
        result = extract_metadata(args.image)
    elif args.steganography:
        result = detect_steganography(args.image)
    else:
        print("Please specify -m for metadata or -s for steganography")
        return
    
    print(result)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Data saved in {args.output}")

if __name__ == "__main__":
    main()
