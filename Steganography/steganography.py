'''
Steganography.py by Antonio Guizar Orozco
This program will encode/decode a secret message in an image file using different ecryption techniques.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    #updates image array with new values, flag= true if updating huffman
    def modify(self, img_array, flag):
        while not flag:
            binary_index=0
            for img in img_array:
                for pixel in img:
                    for i in range(len(pixel)):
                        if binary_index < len(self.binary):
                            #update least significant bit
                            updated_bin= bin(pixel[i])[:-1] + self.binary[binary_index]
                            binary_index+=1
                            #update numbers in each pixel 
                            pixel[i]= int(updated_bin, 2)
                        else:
                            return

    #helper class for decode, will extract all least signigicant bits and convert to plaintext
    def extract(self, img_array, flag):
        secret_message=''
        current_index=0
        extracted_bits= ''
        while not flag:
            for img in img_array:
                for pixel in img:
                    for i in range(len(pixel)):
                        #extract all least significant bits from img_array
                        extracted_bits+= bin(pixel[i])[-1]
                        current_index+=1
            #check for delimiter and only save message up to self.delimiter
            for i in range(0, len(extracted_bits), 8):
                if not extracted_bits[i:i+8] == bin(ord(self.delimiter)):
                    secret_message+= extracted_bits[i:i+8]
                else:
                    return self.codec.decode(secret_message)
            return self.codec.decode(secret_message)
    #uses the codec provided to encode a message and write it to an image file
    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        #print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
            while(True):
                try:
                    shift= int(input('Enter an integer for the shift value [default 3]: '))
                    break
                except (ValueError, TypeError):
                    print('Input must be an integer')
            self.codec.shift= shift
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            #method that modifies the image array
            self.modify(image, False)
            cv2.imwrite(fileout, image)

    #uses codec provided to read an image file and extract the secret message     
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        flag= False
        #print(image) # for debugging

        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
            while(True):
                try:
                    shift= int(input('Enter an integer for the shift value [default 3]: '))
                    break
                except (ValueError, TypeError):
                    print('Input must be an integer')
            self.codec.shift= shift
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        #flag is True when huffman teqnique is used
        if flag:
            pass
        self.text= self.extract(image, False)
                           
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()


