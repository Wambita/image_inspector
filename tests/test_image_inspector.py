"""
Unit tests for Image Inspector
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from modules.metadata_extractor import extract_metadata, convert_to_degrees


class TestMetadataExtractor(unittest.TestCase):
    """Test metadata extraction functionality"""

if __name__ == '__main__':
    unittest.main()