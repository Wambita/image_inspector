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
    def test_convert_to_degrees(self):
        """Test GPS coordinate conversion"""
        result = convert_to_degrees((32, 5, 11.87))
        self.assertAlmostEqual(result, 32.0866, places=3)
    
    def test_convert_to_degrees_none(self):
        """Test GPS conversion with None input"""
        result = convert_to_degrees(None)
        self.assertIsNone(result)
        
class TestSteganographyDetector(unittest.TestCase):
    """Test steganography detection functionality"""
    
    def test_detect_steganography_returns_string(self):
        """Test that steganography detector returns a string"""
        # This would need actual test images
        pass
        

if __name__ == '__main__':
    unittest.main()