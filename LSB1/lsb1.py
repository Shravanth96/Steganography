# -*- coding: utf-8 -*-
"""LSB1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12l23ekecTF2iLeWfNPNgTyqBp1Z_RyFD
"""

from PIL import Image
import numpy as np

def encrypt_pixel(img, byte_array):
    c=-1

    for pix in img:
        c += 1
        try:
                #print(img[c])
                if byte_array[c] == '1':
                    # even
                    if img[c] % 2 == 0:
                        img[c] -= 1
                elif byte_array[c] == '0':
                    # odd
                    if img[c] % 2 != 0:
                        img[c] -= 1
                elif byte_array[c] == ' ':
                    if img[c] % 2 != 0:
                        img[c] -= 1
                #print(img[c],byte_array[c])
        except:
                if img[c] % 2 == 0:
                    img[c] -= 1
                break
    return img

def get_byte(a):
    a_bytes = bytes(a, "ascii")
    return  (' '.join(format(ord(x), '08b') for x in a))


if __name__ == '__main__':
    #'1.png'
    image_name = input('Please Enter Image Name:')
    im = Image.open(image_name)
    x,y = list(im.size)
    rgb = np.asarray(im).reshape(-1)
    new_img = np.array(rgb)
    masg =input('Please enter your message: ')
    enc = get_byte(masg)
    encrypted  = (encrypt_pixel(new_img,enc))
    final_img = encrypted.reshape(y,x,3)
    im = Image.fromarray(final_img)
    im.save("2.png")
    print('Encrypted and Saved')

from PIL import Image
import numpy as np


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return chr(decimal)

def decrypt(pix):
    st = ''
    c=0
    for i in pix:
        c+=1
        if i%2 != 0 and c%9==0:
            break
        elif i%2 == 0 and c%9==0:
            st+=' '
        elif i%2 ==0:
            st+='0'
        elif i%2 !=0:
            st+='1'
    return st

if __name__ == '__main__':
    image_path = input('Please Enter Image Name:')
    im = Image.open(image_path)

    x,y = list(im.size)
    rgb = np.asarray(im).reshape(-1)

    new_img = np.array(rgb)
    de = decrypt(new_img)

    de_array = de.split(' ')

    final_masg =  ''

    for i in de_array:
        final_masg+=binaryToDecimal(int(i))

    print('Message:',final_masg)