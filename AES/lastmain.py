import math
import os
from key import generate
import copy
def letter_to_number(text):
    numbers =[]
    for i in range(len(text)):
       numbers.append(ord(text[i]))
    return numbers
def letter_to_number_26(text):
    numbers =[]
    text=text.upper()
    for i in range(len(text)):
       numbers.append(ord(text[i])-65)

    return numbers
def letter_to_number_25(text):
    numbers =[]
    text=text.upper()
    for i in range(len(text)):
        if ord(text[i])>73:
            numbers.append(ord(text[i])-66)
        else:
            numbers.append(ord(text[i])-65)


    return numbers
def number_to_letter(number):
    text = ""
    for i in range(len(number)):
        text+=(chr(number[i]))
    return text
def number_to_letter_26(number):
    text = ""
    for i in range(len(number)):
        text+=(chr(number[i]%26+65))
    return text
def number_to_letter_25(number):
    text = ""
    for i in range(len(number)):
        if number[i]>8:
            number[i]+=1
        text+=(chr(number[i]+65))
    return text
# create a folder named "output files" and text files
def write_text(text,file_name):
    os.makedirs("ouput files",exist_ok=True)
    with open( "ouput files/"+file_name+".txt", "w+") as output:
        output.write(text)
# Decimal to binary
def decimal_to_binary(num):
    res = bin(num).replace("0b", "")
    if (len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res
# Binary to decimal
def binary_to_decimal(binary):
    binary=int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
# Hexadecimal to binary
def hex_to_binary(s):
    code = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    binary = ""
    for i in range(len(s)):
        binary = binary + code[s[i]]
    return binary
# Binary to hexadecimal
def binary_to_hex(s):
    mpp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
           "1011": 'B',
           "1100": 'C',
           "1101": 'D',
           "1110": 'E',
           "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mpp[ch]

    return hex
sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
def s_box_finder(word):
    sWord = ()
    # loop throug the current word
    for j in range(len(word)):
        for i in range(0,8,2):

            # check first char, if its a letter(a-f) get corresponding decimal
            # otherwise just take the value and add 1
            if word[j][i].isdigit() == False:
                row = ord(word[j][i]) - 54
            else:
                row = int(word[j][i]) + 1

            # repeat above for the seoncd char
            if word[j][i+1].isdigit() == False:
                col = ord(word[j][i+1]) - 54
            else:
                col = int(word[j][i+1]) +1

            # get the index base on row and col (16x16 grid)
            sBoxIndex = (row * 16) - (17 - col)

            # get the value from sbox without prefix
            piece = hex(sbox[sBoxIndex])[2:]

            # check length to ensure leading 0s are not forgotton
            if len(piece) != 2:
                piece = '0' + piece

            # form tuple
            sWord = (*sWord, piece)

    # return string
    return ''.join(sWord)
def xor_with_key(text, key):
    out=""
    for i in range(len(text)):
        out+=str(int(text[i])^int(key[i]))
    return out
def construct_matrix(line):

    # construct a matrix
    text_matrix = []
    for i in range(0, len(line), 8):
        text_matrix.append(line[i:i + 8])
        a0=""
        a1 = ""
        a2 = ""
        a3 = ""
    for i in range(0,len(text_matrix),1):

        a0+=text_matrix[i][0:2]
        a1 += text_matrix[i][2:4]
        a2 += text_matrix[i][4:6]
        a3 += text_matrix[i][6:8]

    text_matrix=[]
    text_matrix.append(a0)
    text_matrix.append(a1)
    text_matrix.append(a2)
    text_matrix.append(a3)

    return text_matrix
def shift_the_rows(s):
    a0 = ""
    a1 = ""
    a2 = ""
    a3 = ""

    for i in range(0, len(s), 1):
        a0 += s[i][0:2]
        a1 += s[i][2:4]
        a2 += s[i][4:6]
        a3 += s[i][6:8]

    text_matrix = []
    text_matrix.append(a0)
    text_matrix.append(a1)
    text_matrix.append(a2)
    text_matrix.append(a3)

    ss=["","","",""]

    ss[0]=text_matrix[0]
    ss[1] = text_matrix[1][2:8] + text_matrix[1][:2]
    ss[2] = text_matrix[2][4:] + text_matrix[2][:4]
    ss[3] = text_matrix[3][6:] + text_matrix[3][:6]

    return ss
def rotate(text_matrix):
    a0 = ""
    a1 = ""
    a2 = ""
    a3 = ""


    for i in range(0, len(text_matrix), 1):
        a0 += text_matrix[i][0:2]
        a1 += text_matrix[i][2:4]
        a2 += text_matrix[i][4:6]
        a3 += text_matrix[i][6:8]

    text_matrix = []
    text_matrix.append(a0)
    text_matrix.append(a1)
    text_matrix.append(a2)
    text_matrix.append(a3)

    return text_matrix
def gf_multiply(first_vector,second_vector):
    result=[]
    for i in range(len(first_vector)):
        if first_vector[i]==1:
            result.append(second_vector[i*8:i*8+8])
        elif first_vector[i]==2:
            result.append(second_vector[i*8+1:i*8+8]+"0")
        elif first_vector[i]==3:
            result.append(xor_with_key( second_vector[i*8+1:i*8+8] + "0",second_vector[i*8:i*8+8]))

    final= xor_with_key(xor_with_key(xor_with_key(result[0],result[1]),result[2]),result[3])
    return final
def gf_multiply_8(first_vector,second_vector):
    result=[]
    for i in range(len(first_vector)):
        if first_vector[i]==1:
            result.append(second_vector[i*8:i*8+8])
        elif first_vector[i]==2:
            times_2=decimal_to_binary(binary_to_decimal(second_vector[i*8:i*8+8])*2)
            times_2=str(times_2)
            if  len(times_2)>8:
                times_2=xor_with_key(times_2[4:],"00011011")
            elif len(times_2)<8:
                times_2="0000"+times_2
            result.append(times_2)
        elif first_vector[i]==3:
            times_2 = decimal_to_binary(binary_to_decimal(second_vector[i * 8:i * 8 + 8]) * 2)
            times_2 = str(times_2)
            if len(times_2) > 8:
                times_2 = xor_with_key(times_2[4:], "00011011")
            elif len(times_2) < 8:
                times_2 = "0000" + times_2

            result.append(xor_with_key( times_2,second_vector[i*8:i*8+8]))

    final= xor_with_key(xor_with_key(xor_with_key(result[0],result[1]),result[2]),result[3])
    return final
def encrypt_block( plaintext,key):


    original_key=key
    #plain text to binary
    plaintext_binary=hex_to_binary(plaintext)

    #key to binary
    key=generate(key)
    for i in range(len(key)):
        key[i] = hex_to_binary(key[i])

    text_after_first_round=xor_with_key(plaintext_binary, key[0])

    text_after_first_round=binary_to_hex(text_after_first_round)




    for ii in range(10):
        # construct a matrix
        text_matrix = construct_matrix(text_after_first_round)

        a1=s_box_finder(text_matrix)

        a1=construct_matrix(a1)


        a1=shift_the_rows(a1)
        #rotate
        a1=rotate(a1)
        #make binary
        for i in range(len(a1)):
            a1[i]=hex_to_binary(a1[i].upper())


        shift_matrix=[[2 ,3 ,1 ,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
        result=[[2 ,3 ,1 ,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
        for i in range(4):
            for j in range(4):
                result[i][j]=gf_multiply_8(shift_matrix[i],a1[j])
        if ii != 9:
            a1=[]
            for i in range(len(result)):
                a1.append(''.join(result[i]))
        for i in range(4):
            a1[i]=binary_to_hex(a1[i])
        # print(a1)
        a1=rotate(a1)
        if ii==9:
            a1=rotate(a1)
        a1=(''.join(a1))
        a1=hex_to_binary(a1)



        #must convert to one line in binary
        text_after_first_round=xor_with_key(a1, (key[ii+1]))
        # print(binary_to_hex(a1))
        # print(binary_to_hex(key[ii+1]),"hjgfj")

        text_after_first_round=binary_to_hex(text_after_first_round)
        # print(text_after_first_round)



    return text_after_first_round
############################################################################################################
# print(encrypt_block("54776F204F6E65204E696E652054776F".upper(),"5468617473206D79204B756E67204675".lower()))
print("enter 2 lines , a 32 hex key and a 32 hex plain text.")
key=input()
plain_text=input()
print("cipher text of ",plain_text," is : ",encrypt_block(plain_text.upper(),key.lower()))
input()
