from PIL import Image
import os

def encrypt_decrypt_image(image_path, key, mode):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure RGB mode

        width, height = img.size
        pixels = img.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                if mode == "encrypt":
                    r_new = r ^ key
                    g_new = g ^ key
                    b_new = b ^ key
                elif mode == "decrypt":
                    r_new = r ^ key
                    g_new = g ^ key
                    b_new = b ^ key
                else:
                    raise ValueError("Invalid mode.")

                pixels[x, y] = (r_new, g_new, b_new)

        output_path = f"{'encrypted' if mode == 'encrypt' else 'decrypted'}_{os.path.basename(image_path)}"
        img.save(output_path)
        print(f"{mode.capitalize()}ed image saved as '{output_path}'.")

    except Exception as e:
        print("Error:", e)

def main():
    print("=== Image Encryptor / Decryptor ===")
    path = input("Enter path to the image: ").strip()
    if not os.path.exists(path):
        print("Image file not found.")
        return

    mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        return

    try:
        key = int(input("Enter a key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Must be an integer between 0 and 255.")
        return

    encrypt_decrypt_image(path, key, mode)

if __name__ == "__main__":
    main()
