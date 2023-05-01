import numpy as np
from PIL import Image
import sys, random

EOF_MARKER = '$eof!' # end delimeter 
confs = {'RGB':[0,3], 'RGBA':[1,4]}


def calculate_min_size(number_of_bits):
    """Calculates the minimum image size needed to contain number_of_bits"""
    min_pxls = number_of_bits//3 # 1 pixel = 3 bits stored
    return min_pxls

def get_num_rand(used_pixels, num_of_pixels):
    n = random.randint(0, num_of_pixels)
    while n in used_pixels:
        n = random.randint(0, num_of_pixels)
    used_pixels.add(n)
    return n

def hide_data(seed, input_data, output_file, carrier):
    """
    Takes a seed, some data, a filename for the output image and a carrier. 
    This function hides data inside the carrier using LSB technique
    """
    byte_written = 0
    img = Image.open(carrier, 'r')
    width, height = img.size
    matrix = np.array(list(img.getdata()))
    generator = random.seed(seed)
    used_pixels = set()
    # Get the configuration: is RGB or RGBA?
    conf = confs[img.mode]
    num_of_pixels = matrix.size//conf[1]
    print("Hiding: ",input_data)
    # Append a marker. When this marker is encountered, no more hidden data can be found next.
    input_data += EOF_MARKER
    binary_enc = "".join([format(ord(ch), "08b") for ch in input_data])
    min_size = calculate_min_size(len(binary_enc))
    print("Minimum size needed is {} pixels and the carrier has: {}".format(min_size, num_of_pixels))
    if min_size >= num_of_pixels:
        print("ERROR: The image is not big enough to carry the data with the specified passphrase")
        sys.exit(1)
    start_pixel = get_num_rand(used_pixels, num_of_pixels)
    while byte_written != len(input_data):
        bit_i = 0
        while bit_i != 8:
            px = matrix[start_pixel]
            # colors: Red, Green and Blue
            for c in range(conf[0], conf[1]):
                if bit_i == 8:
                    break
                # Because of Least Significant Bit, we want to modify the last bit of every color
                color = matrix[start_pixel][c]
                lsb = color&1
                # Here, we just use bit manipulation to modify the last bit of the color number
                if lsb != int(binary_enc[(byte_written*8)+bit_i]):
                    color = color>>1 # erase last bit
                    color = color<<1 # zero last bit
                    if lsb == 0: # it means that byte[bit_i]=1, so I need to encode 1
                        color = color|1
                    matrix[start_pixel][c] = color
                bit_i += 1
            start_pixel = get_num_rand(used_pixels, num_of_pixels)
        byte_written += 1
        bit_i = 0
        start_pixel = get_num_rand(used_pixels, num_of_pixels)

    out_img = Image.fromarray(np.uint8(matrix.reshape(height, width, conf[1])), img.mode)
    out_img.save(output_file)
    print("All done!")

def retrieve_data(seed, input_file):
    """
    Takes a passhprase and an image. Outputs the hidden data inside the image, if any.
    """
    img = Image.open(input_file, 'r')
    width, height = img.size
    matrix = np.array(list(img.getdata()))
    # Get the configuration: is RGB or RGBA?
    conf = confs[img.mode]
    num_of_pixels = matrix.size//conf[1]
    generator = random.seed(seed)
    used_pixels = set()
    start_pixel = get_num_rand(used_pixels, num_of_pixels)
    bit_i = 7
    byte = 0
    message = ""
    end = False
    while (end == False):
        while (bit_i >= 0):
            px = matrix[start_pixel]
            # colors: Red, Green and Blue
            for c in range(conf[0], conf[1]):
                if bit_i >= 0:
                    # We are getting the LSB of the pixel color, and then we shift it to the left accordingly
                    byte += (px[c]&1)<<bit_i
                    bit_i -= 1
                else:
                    break
            start_pixel = get_num_rand(used_pixels, num_of_pixels)
        if start_pixel>=num_of_pixels:
            break
        # decoded 1 byte
        message += chr(byte)
        # have I encountered the eof_marker? If yes, the decoding process is done
        if message[-len(EOF_MARKER):] == EOF_MARKER:
            end = True
        byte = 0
        bit_i = 7
        start_pixel = get_num_rand(used_pixels, num_of_pixels)
    
    if end == False:
        print("Nothing found in this image")
    else:
        print("All done!")
        print("The hidden message is: ")
        print(message[:len(message)-len(EOF_MARKER)])
    return message[:len(message)-len(EOF_MARKER)]

def main():

    exit = 0 
    while exit != 1:
        print("1. Encrypt")
        print("2. Decrypt")
        print('3. Exit')
        choice = input("Enter any option: ")
        # Break
        if choice == "3":
            exit = 1
            continue
        if choice == "1":
            original_image = input("Enter file name: ")
            input_data = input("Enter input data: ")
            seed_value = input("Enter the key: ")
            output = input("Enter output filename: ")
            hide_data(seed_value, input_data, output, original_image)

        if choice == "2":
            input_image = input("Enter the input file: ")
            seed_value = input("Enter the key: ")
            retrieve_data(seed_value, input_image)

if __name__ == '__main__':
    main()
