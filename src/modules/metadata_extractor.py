from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def convert_to_degrees(value):
    """Convert GPS coordinates to degrees"""
    if not value:
        return None
    d, m, s = value
    return float(d) + float(m) / 60 + float(s) / 3600

def extract_metadata(image_path):
    """Extract metadata from image"""
    img = Image.open(image_path)
    exif = img.getexif()
    
    result = []