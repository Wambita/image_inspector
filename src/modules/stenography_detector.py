from PIL import Image

def detect_steganography(image_path):
    """Detect hidden data using LSB steganography"""
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    binary_data = ""

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            if isinstance(pixel, int):
                binary_data += str(pixel & 1)
            else:
                for value in pixel[:3]:
                    binary_data += str(value & 1)

     # Convert binary to text
    text = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]

        if len(byte) == 8:
            char = chr(int(byte, 2))

            if char == '\0':
                break

            if 32 <= ord(char) <= 126 or char in '\n\r\t':
                text += char
            else:
                if len(text) > 50:
                    break

    if "BEGIN PGP" in text or len(text) > 50:
        return text.strip()
    
    return "No hidden data detected"