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
      
def hide_bits_in_pixels(pixel, secret_bits):
    #converts the RGB pixel values into binary
    #pixel = (0,0,0) into [  "00010011","01100110" "10101000"]
    pixel_binary = convert_pixel_to_binary(pixel)

    #create an empty collection for the modified RGB values
    new_pixel_values = []

    #FOR each binary color value in the pixel
    for i in range(3):
        altered_binary = replace_lsb(pixel_binary[i], secret_bits[i])
        decimal_value = binary_to_decimal(altered_binary)
        new_pixel_values.append(decimal_value)

    return tuple(new_pixel_values)

def text_to_binary(message):

    #create an empty string for all binary bits
    binary_bits = ""

    #FOR each character in message
    for char in message:
        #convert character into its numeric value
        numeric_value= ord(char)
        #convert that number into 8-bit binary
        binary = format(numeric_value, "08b")
        #add those 8 bits to the binary string
        binary_bits += binary

    #return the complete binary string
    return binary_bits




def main():
    filename = "sparrow.png"
    x = int(input("Enter The Value Of The X Pixel: "))
    y = int(input("Enter The Value Of The Y Pixel: "))
    returned_image = open_image(filename)

    given_pixels = get_pixel(x,y, returned_image)
    print(given_pixels)

    pixel_binary = (convert_pixel_to_binary(given_pixels))

    #altered_binary = (replace_lsb(binary_value=pixel_binary[0],secret_bit="1"))

    #print(binary_to_decimal(altered_binary))



if __name__ == "__main__":
    main()