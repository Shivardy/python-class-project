# importing libraries
from PIL import Image
import urllib.request
import os
import binascii
import time

# function to convert rgb values to hex values


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# function to convert hex values to rgb


def hex_to_rgb(hexcode):
    # strippting the # sign fromt he hex code
    hexcode = hexcode.lstrip('#')
    # looping through hexvalues and coverting to rgb
    return tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4))

# function to convert string values to binary


def string_to_binary(message):
    return bin(int(binascii.hexlify(message.encode()), 16))[2:]

# function to convert binary values to string


def binary_to_string(binary):
    return binascii.unhexlify('%x' % (int('0b'+binary, 2))).decode()

# function to store the index values in the hexcode of the pixel


def storing(hexcode, index):
    # checking if the last code in the hexvalue is in 0 to 5 then replace it with index
    return hexcode[:-1] + index if hexcode[-1] in ('0', '1', '2', '3', '4', '5') else None

# function to get the stored index value in the hexcode.


def retriving(hexcode):
    # checking if the last character of the hexcode is either 0 or 1 then return the last hexcode.
    return hexcode[-1] if hexcode[-1] in ('0', '1') else None

# function to handle encryption which takes message, image as arguments.


def encryption(message, image):
    # generating a filename for the image
    name = "images/"+str(int(time.time()*10000000000000000))+".jpg"
    # retriving the image from api and storing it locally
    urllib.request.urlretrieve(image, name)
    # opening the image with pip
    img = Image.open(name)
    # converting the message into binary and appending some buffer at the end of the message
    binary = string_to_binary(message) + '1111111111111110'
    # checking if the image is editable.
    if img.mode in ('RGBA'):
        # converting the image to rgba format
        img = img.convert('RGBA')
        # getting the pixel data of the image
        imgPixles = img.getdata()
        # creating array to store new pixel data
        newPixelData = []
        # variable to track index of the binary message
        index = 0
        # looping over each pixel
        for pixel in imgPixles:
            # checking if the length of the binary message is less than index.
            if(index < len(binary)):
                # converting rgb pixel to hexvalues and passing to storing function along with binary value
                newpix = storing(
                    rgb_to_hex(pixel[0], pixel[1], pixel[2]), binary[index])
                # checking if the new pixel has any data
                if newpix == None:
                    # if new pixel don't have any data directly append to new pixel data array
                    newPixelData.append(pixel)
                else:
                    # converthing the new pixel hex value to rgb data
                    r, g, b = hex_to_rgb(newpix)
                    # stroing new pixel in new pixel data array
                    newPixelData.append((r, g, b, 255))
                    # updating the index
                    index += 1
            else:
                # once the entire message is done processing directly append the extra pixels
                newPixelData.append(pixel)
        # generating image from raw pixel data
        img.putdata(newPixelData)
        # saving the image
        img.save(name, "PNG")
        # retunring the image name
        return name[7:]
    return "error"

# function to handle the decryption


def decryption(filename):
    # opening the image
    img = Image.open("images/"+filename)
    # declaring variable to hold the binary data
    binary = ''
    # checking if the image is editable.
    if img.mode in ("RGBA"):
        # converting the image to rgba format
        img = img.convert("RGBA")
        # getting pixel data of the image
        imgPixles = img.getdata()
        # looping through each pixel
        for pixel in imgPixles:
            # converting pixel to rgb and retriving the data in that pixel
            index = retriving(rgb_to_hex(pixel[0], pixel[1], pixel[2]))
            # if there is no data in the pixel then pass
            if index == None:
                pass
            else:
                # if there is data in the pixel append it to the binary
                binary = binary + index
                # remove the buffer from the binary data
                if (binary[-16:] == "1111111111111110"):
                    # return the binary after converting it to string
                    return binary_to_string(binary[:-16])
        return binary_to_string(binary)
    return "error"
