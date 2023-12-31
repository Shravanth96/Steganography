# -*- coding: utf-8 -*-
"""Stegnography_F5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgOePTXw2ZjaISp7XPTmzvNL41LYLshi
"""

!pip install stegano

from PIL import Image
from stegano import lsb
from google.colab import files

def upload_image():
    # Use the Colab file uploader to upload an image
    uploaded = files.upload()

    # Get the first uploaded file
    image_path = list(uploaded.keys())[0]

    return image_path

def encode_f5(encoded_image_path):
    # Prompt the user to upload an image
    print("Upload the original image:")
    original_image_path = upload_image()

    # Open the original image
    img = Image.open(original_image_path)

    # Take user input for the secret message
    secret_message = input("Enter the secret message: ")

    # Embed the secret message using F5 steganography
    encoded_img = lsb.hide(img, secret_message)

    # Save the encoded image
    encoded_img.save(encoded_image_path)

def decode_f5(encoded_image_path):
    try:
        # Open the encoded image
        encoded_img = Image.open(encoded_image_path)

        # Extract the hidden message using F5 steganography
        decoded_message = lsb.reveal(encoded_img)

        return decoded_message
    except lsb.SteganographyException as e:
        return f"Error decoding: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Example Usage:
# encode_f5("encoded_image.png")
# secret_message = decode_f5("encoded_image.png")
# print(secret_message)

encode_f5("original_image.png")

secret_message = decode_f5("original_image.png")
print(secret_message)