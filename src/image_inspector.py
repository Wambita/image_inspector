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