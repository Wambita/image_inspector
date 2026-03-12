# Image Inspector 

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional command-line tool for analyzing images to extract hidden information including metadata and steganographic data.

## Features

- **Metadata Extraction**: Extract EXIF data including geolocation, device information, and timestamps
- **Steganography Detection**: Detect and extract hidden data using LSB (Least Significant Bit) techniques
- **Simple CLI**: Easy-to-use command-line interface

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

### Quick Start
```bash
# Clone the repository
git clone https://learn.zone01kisumu.ke/git/shfana/image-inspector.git
cd image-inspector

# Install dependencies
pip install -r requirements.txt
```

### Development Installation
```bash
pip install -e .
```

## Usage

### Display Help
```bash
python3 src/image-inspector.py --help
```

### Extract Metadata
```bash
python3 src/image-inspector.py -m image.jpeg
```

### Extract Metadata and Save to File
```bash
python3 src/image-inspector.py -m -o metadata.txt image.jpeg
```

### Detect Steganography
```bash
python3 src/image-inspector.py -s image.jpeg
```

### Detect Steganography and Save to File
```bash
python3 src/image-inspector.py -s -o hidden_data.txt image.jpeg
```

## Command-Line Options

- `-m, --metadata`: Extract metadata from the image (geolocation, device info, date/time)
- `-s, --steganography`: Detect and extract hidden data using steganography techniques
- `-o, --output "FileName"`: Specify the file name to save output
- `--help`: Display help message

## Example Outputs

### Metadata Extraction
```
$ python3 src/image-inspector.py -m -o metadata.txt image.jpeg
Lat/Lon: (13.731) / (-1.1373)
Device: Canon EOS 5D Mark III
Date: 2023-07-20 14:32:10
Data saved in metadata.txt
```

### Steganography Detection
```
$ python3 src/image-inspector.py -s -o hidden_data.txt image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: 01
...
-----END PGP PUBLIC KEY BLOCK-----
Data saved in hidden_data.txt
```

## How It Works

### Metadata Extraction
The tool uses the PIL (Pillow) library to read EXIF data embedded in images. It specifically extracts:
- GPS coordinates (latitude/longitude) from GPSInfo tags
- Camera make and model
- Date and time the photo was taken

### Steganography Detection
The tool implements LSB (Least Significant Bit) extraction:
1. Reads each pixel's RGB values
2. Extracts the least significant bit from each color channel
3. Reconstructs the hidden message from the binary data
4. Detects PGP keys and other hidden text

## Ethical and Legal Considerations

⚠️ **IMPORTANT**: This tool is for educational purposes only.

- **Get Permission**: Always obtain explicit permission before analyzing any image
- **Respect Privacy**: Handle metadata and hidden data responsibly
- **Follow Laws**: Adhere to relevant laws regarding data privacy and digital media analysis
- **Educational Use**: This tool is designed for learning about digital forensics and cybersecurity

**Disclaimer**: The institution and developers are not responsible for misuse of the techniques and tools demonstrated. Ensure all activities comply with legal and ethical standards.

## Project Structure

```
image-inspector/
├── src/
│   ├── __init__.py
│   ├── image-inspector.py      # Main CLI entry point
│   └── modules/
│       ├── __init__.py
│       ├── metadata_extractor.py
│       └── steganography_detector.py
├── tests/
│   └── test_image_inspector.py
├── docs/
│   └── USAGE.md
├── examples/
│   └── example_usage.py
├── requirements.txt
├── setup.py
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## Testing

Run unit tests:
```bash
python3 -m pytest tests/
```

Test with example images:
```bash
python3 examples/example_usage.py image-example1.jpeg
```

## Troubleshooting

- **No metadata found**: The image may not contain EXIF data (common in screenshots or edited images)
- **No hidden data detected**: The image may not contain steganographic data, or it uses a different technique
- **Import errors**: Ensure Pillow is installed: `pip install Pillow`

## Technical Details

- **Language**: Python 3
- **Dependencies**: Pillow (PIL Fork)
- **Supported Formats**: JPEG, PNG, and other formats supported by Pillow
- **Steganography Method**: LSB (Least Significant Bit) extraction

## Future Enhancements

Potential improvements for this tool:
- Support for additional steganography techniques
- GUI interface using Tkinter or PyQt
- Batch processing of multiple images
- More detailed metadata reporting
- Support for other hidden data formats

## Contributing
### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to all functions
- Keep functions minimal and focused
- Write clear commit messages

### Testing

Ensure your code works with the provided test images before submitting.

### Ethical Guidelines

All contributions must adhere to ethical standards:
- No malicious code
- Respect privacy and data protection laws
- Educational purpose only

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Pillow](https://python-pillow.org/) for image processing
- Inspired by digital forensics and cybersecurity research

## Support

For questions or issues, please open an issue on GitHub.
