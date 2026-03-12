from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image-inspector",
    version="1.0.0",
    author="Digital Forensics Team",
    description="A tool for analyzing images and extracting hidden information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/image-inspector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "image-inspector=src.image-inspector:main",
        ],
    },
)
