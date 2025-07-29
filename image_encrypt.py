from PIL import Image
import os

# Encryption key (must be same for decryption)
KEY = 123

def encrypt_image(input_path, output_path):
    image = Image.open(input_path)
    encrypted = Image.new(image.mode, image.size)
    
    pixels = list(image.getdata())
    encrypted_pixels = [(r ^ KEY, g ^ KEY, b ^ KEY) for r, g, b in pixels]

    encrypted.putdata(encrypted_pixels)
    encrypted.save(output_path)
    print(f"Image encrypted and saved to: {output_path}")

def decrypt_image(input_path, output_path):
    # Since XOR is symmetric, we just reapply the same key
    encrypt_image(input_path, output_path)

def main():
    print("1. Encrypt Image\n2. Decrypt Image")
    choice = input("Enter choice (1/2): ")

    input_path = input("Enter path to input image: ")
    output_path = input("Enter path to save output image: ")

    if not os.path.exists(input_path):
        print("❌ Image not found!")
        return

    if choice == '1':
        encrypt_image(input_path, output_path)
    elif choice == '2':
        decrypt_image(input_path, output_path)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
