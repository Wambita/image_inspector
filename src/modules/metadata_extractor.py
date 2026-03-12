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
    
    # Extract EXIF data if available
    if exif:
        metadata = {}
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
        
        # Extract GPS info
        gps_info = exif.get_ifd(0x8825) if 0x8825 in exif else None
        lat, lon = None, None
        if gps_info:
            gps_data = {}
            for key in gps_info.keys():
                decode = GPSTAGS.get(key, key)
                gps_data[decode] = gps_info[key]
            
            lat = convert_to_degrees(gps_data.get('GPSLatitude'))
            if gps_data.get('GPSLatitudeRef') == 'S':
                lat = -lat
            lon = convert_to_degrees(gps_data.get('GPSLongitude'))
            if gps_data.get('GPSLongitudeRef') == 'W':
                lon = -lon
        
        if lat and lon:
            result.append(f"Lat/Lon: ({round(lat, 4)}) / ({round(lon, 4)})")
        
        make = metadata.get('Make', '').strip()
        model = metadata.get('Model', '').strip()
        if make or model:
            device = f"{make} {model}".strip()
            result.append(f"Device: {device}")
        
        datetime = metadata.get('DateTime') or metadata.get('DateTimeOriginal')
        if datetime:
            result.append(f"Date: {datetime}")
    
    # Always show basic image info
    import os
    file_size = os.path.getsize(image_path)
    result.append(f"File: {os.path.basename(image_path)}")
    result.append(f"Size: {file_size // 1024} KB")
    result.append(f"Dimensions: {img.size[0]}x{img.size[1]} pixels")
    result.append(f"Format: {img.format}")
    result.append(f"Mode: {img.mode}")
    
    return '\n'.join(result) if result else "No information found"
