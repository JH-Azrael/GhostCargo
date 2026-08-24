#Author: Jonathan Hall
#Project: Ghost Cargo

from PIL import Image

def open_image(filename):
    image = Image.open(filename)
    return image

def get_pixel(x, y, image):
    pixels = image.getpixel((x,y))
    return pixels

def convert_pixel_to_binary(pixels):
    converted_values = []
    for values in pixels:
        converted = format(values, "08b")
        converted_values.append(converted)
    return converted_values       

def replace_lsb(binary_value, secret_bit):
    broken_binary = binary_value[:-1]
    new_binary = broken_binary+(secret_bit)
    return new_binary


def binary_to_decimal(binary_value):
    decimal = int(binary_value, base=2)
    return decimal
      

def main():
    filename = "sparrow.png"
    x = int(input("Enter The Value Of The X Pixel: "))
    y = int(input("Enter The Value Of The Y Pixel: "))
    returned_image = open_image(filename)

    given_pixels = get_pixel(x,y, returned_image)
    print(given_pixels)

    pixel_binary = (convert_pixel_to_binary(given_pixels))

    altered_binary = (replace_lsb(binary_value=pixel_binary[0],secret_bit="1"))

    print(binary_to_decimal(altered_binary))



main()