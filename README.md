# Image Encryptor/Decryptor

## Overview
This project is a simple yet effective image encryption and decryption tool that uses XOR bitwise operation to secure image files. It was developed as Task 2 for the Prodigy InfoTech internship program.

## Features
- Encrypt any image using a custom numeric key (0-255)
- Decrypt previously encrypted images using the same key
- Simple command-line interface
- Works with various image formats (JPG, PNG, etc.)

## Requirements
- Python 3.x
- PIL (Python Imaging Library) / Pillow

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/image-encryptor-decryptor.git
   cd image-encryptor-decryptor
   ```

2. Install the required dependencies:
   ```
   pip install pillow
   ```

## Usage
1. Run the script:
   ```
   python task2.py
   ```

2. Follow the prompts:
   - Enter the path to your image file
   - Choose whether to encrypt or decrypt
   - Enter a numeric key between 0-255

3. The processed image will be saved in the same directory with a prefix of either "encrypted_" or "decrypted_".

## How It Works
The program uses the XOR (exclusive OR) bitwise operation to modify each RGB value of every pixel in the image. The same key is used for both encryption and decryption, making it a symmetric encryption method.

## Example
Original image → Encrypt with key 123 → Encrypted image
Encrypted image → Decrypt with key 123 → Original image

## Note
For successful decryption, you must use the same key that was used for encryption.

## License
This project is open source and available under the [MIT License](LICENSE).

## Author
Created as part of the Prodigy InfoTech internship program.