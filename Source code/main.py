# from numpy import array
# from numpy import dot
# import numpy as np
import math
import os
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

def caesar():
    lines =[]
    key =0
    cipher_text=""

    #open plain text file
    with open( "input files/Caesar/caesar_plain.txt", "r+") as input:
        for line in input:
            lines.append(letter_to_number(line))
    # open key file
    with open("input files/all keys/caesar_key.txt", "r+") as input:
        for line in input:
            key =line
            if int(key) >26:
                key-=26


    # add key to plain text
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]!=10:
                lines[i][j]+=int(key)

    # loop the letters
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not ((lines[i][j]>97 and lines[i][j]<123) or (lines[i][j]>64 and lines[i][j] <91) or lines[i][j] ==10):
                lines[i][j]-=26


    # convert numbers to letters
    for i in range(len(lines)):
        cipher_text +=number_to_letter(lines[i])
    return cipher_text

def hill_cipher():
    lines = []
    matrix_multiplication_out=[]
    key = ""
    cipher_text = ""
    matrix_length = 0
    # open plain text file
    with open("Input Files\Hill\hill_plain.txt", "r+") as input:
        for line in input:
            lines.append(letter_to_number_26(line))
    # open key file
    with open("input files/all keys/hill_key.txt", "r+") as input:
        for line in input:
            key += line


    #turn key into numbers
    key=key.split()
    for i in range(len(key)):
        key[i]=int(key[i])
    # build key as a matrix
    matrix_length=math.sqrt((len(key)))
    for i in range(len(lines)):
        #remove \n and
        if lines[i][len(lines[i])-1]==-55:
            lines[i].remove(-55)
        #add padding
        while True:
            if len(lines[i])%matrix_length!=0:
                lines[i].append(lines[i][len(lines[i])-1])
            else:
                break
        # loop on every letter in lines[i]
        for j in range(0,int(len(lines[i])),int(matrix_length)):

            # multiply the key by the plain text
            for row in range(int(matrix_length)):
                k=0
                for column in range(int(matrix_length)):
                    k+=key[column+row*int(matrix_length)]*lines[i][j+column ]

                matrix_multiplication_out.append(k)
        #append the matrix_multiplication_out to lines and clear matrix_multiplication_out
        lines[i]=list(matrix_multiplication_out)
        matrix_multiplication_out.clear()

    #turn numbers into text
    for i in range(len(lines)):
        cipher_text +=number_to_letter_26(lines[i])+"\n"

    return cipher_text

def Vigenere(mode=False):
    lines = []
    key = ""
    cipher_text = ""

    # open plain text file
    with open("input files/Vigenere/Vigenere_plain.txt", "r+") as input:
        for line in input:
            lines.append(letter_to_number_26(line))
    # open key file
    with open("input files/all keys/Vigenere_key.txt", "r+") as input:
        for line in input:
            key += line

    # repeating mode
    if mode==False:
        for i in range(len(lines)):
            #remove \n
            if lines[i][len(lines[i]) - 1] == -55:
                lines[i].remove(-55)
            #repeat the key n times
            key=line
            key=key*int(len(lines[i])/len(key))+key[0:len(lines[i])%len(key)]
            #encrypt the line

            for j in range(len(lines[i])):
                lines[i][j]=lines[i][j]+letter_to_number_26(key)[j]
            lines[i] = number_to_letter_26(lines[i])

    # auto mode
    if mode == True:
        for i in range(len(lines)):
            #remove \n
            if lines[i][len(lines[i]) - 1] == -55:
                lines[i].remove(-55)
            #complete the key with message
            key=line

            key=key+number_to_letter_26(lines[i])[0:len(lines[i])-len(key)]
            #encrypt the line

            for j in range(len(lines[i])):
                lines[i][j]=lines[i][j]+letter_to_number_26(key)[j]
            lines[i] = number_to_letter_26(lines[i])

    for i in range(len(lines)):
        cipher_text+=lines[i]+"\n"
    return cipher_text


def Vernam():
    lines = []
    key = ""
    cipher_text = ""

    # open plain text file
    with open("input files/Vernam/Vernam_plain.txt", "r+") as input:
        for line in input:
            lines.append(letter_to_number_26(line))
    # open key file
    with open("input files/all keys/Vernam_key.txt", "r+") as input:
        for line in input:
            key += line

    # repeating mode

    for i in range(len(lines)):
        # remove \n
        if lines[i][len(lines[i]) - 1] == -55:
            lines[i].remove(-55)

        # encrypt the line

        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j] + letter_to_number_26(key)[j]
        lines[i] = number_to_letter_26(lines[i])

    for i in range(len(lines)):
        cipher_text += lines[i] + "\n"
    return cipher_text

def play_fair():
    lines = []
    key = ""
    cipher_text = ""
    matrix = ""
    matrix_multiplication_out = []
    # open plain text file
    with open("Input Files\playfair\playfair_plain.txt", "r+") as input:
        for line in input:
            lines.append(letter_to_number_25(line))
    # open key file
    with open("input files/all keys/PlayFair_key.txt", "r+") as input:
        for line in input:
            key += line
    #remove \n
    for i in range(len(lines)):
        if lines[i][len(lines[i])-1]==-55:
            lines[i].remove(-55)
    #back to letters
    for i in range(len(lines)):
        lines[i]=number_to_letter_25(lines[i])

    # add x to plain text before repeating letters
    # for i in range(len(lines)):
    #     letter=""
    #     index=0
    #     offset=0
    #     for j in range(len(lines[i])):
    #         if letter!=lines[i][j]:
    #             letter=lines[i][j]
    #             index=j
    #         elif letter ==lines[i][j]: #add x or y
    #             if index%2==0:
    #                 if lines[i][j]!="X":
    #                     lines[i]=(list(lines[i]))
    #                     lines[i][j]="X"+lines[i][j]
    #                     "".join(lines[i])
    #
    #                 elif lines[i][j]!="Y":
    #                     lines[i] = (list(lines[i]))
    #                     lines[i][j] = "Y" + lines[i][j]
    #                     "".join(lines[i])
    #                 offset+=1
    #             elif index%2==1:
    #                 letter = lines[i][j]
    #                 index=offset+j




    # to numbers
    for i in range(len(lines)):
        lines[i]=letter_to_number_25(lines[i])

    # # add x to plain text before repeating letters
    i=0
    while i<len(lines):
        letter = 100
        index = 0
        offset = 0

        for j in range(len(lines[i])):
            if letter != lines[i][j]:
                letter = lines[i][j]
                index = j
            elif letter == lines[i][j]:  # add x or y

                if index % 2 == 0:
                    if lines[i][j] != 22:
                        lines[i].insert(j,22)


                    elif lines[i][j] != 23:
                        lines[i].insert(j, 23)
                    i -= 1
                    break
                elif index%2==1:
                    letter = lines[i][j]
                    index = j

        i+=1



    # to letters
    for i in range(len(lines)):
        lines[i]=number_to_letter_25(lines[i])

    # #add x to the end if odd
    for i in range(len(lines)):
        if len(lines[i])%2==1:
            if lines[i][len(lines[i])-1]!="X":
                lines[i]+="X"
            elif lines[i][len(lines[i])-1]!="Y":
                lines[i]+="Y"


    # to numbers
    for i in range(len(lines)):
        lines[i]=letter_to_number_25(lines[i])

    # turn key to matrix
    key=letter_to_number_25(key)
    matrix=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    matrix_minus=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    # remove dublicate from the key
    for i in range(len(key)):
        for j in range(1,len(key)-i):
            if key[i]==key[j+i]:
                key[j+i]=-1000
    for i in range(len(key)):
        try:
            key.remove(-1000)
        except:
            pass

    #remove the key from the matrix
    for i in range(len(matrix)):
        for j in range(len(key)):
            if matrix[i]==key[j]:
                matrix_minus.remove(key[j])

    #extend the matrix to the key
    key.extend(matrix_minus)
    #make key into matrix form
    matrix_key=[]
    for i in range(5):
        matrix_key.append(key[i*5:i*5+5])
    #search
    row1=-1
    column1=-1
    row2=-1
    coumn2=-1
    for i in range(len(lines)):
        for j in range(0,len(lines[i]),2):
            for k in range(5):
                for n in range(5):
                    if lines[i][j]==matrix_key[k][n]:
                        row1 =k
                        column1=n
            for k in range(5):
                for n in range(5):
                    if lines[i][j+1]==matrix_key[k][n]:
                        row2=k
                        column2=n
            if row1!=row2 and column1!= column2:
                lines[i][j]=matrix_key[row1][column2]
                lines[i][j+1]=matrix_key[row2][column1]
            elif row1==row2:
                lines[i][j] = matrix_key[row1][(column1+1)%5]
                lines[i][j + 1] = matrix_key[row2][(column2+1)%5]
            elif column1==column2:
                lines[i][j] = matrix_key[(row1+1)%5][column2]
                lines[i][j + 1] = matrix_key[(row2+1)%5][column1]


        # to letters
    for i in range(len(lines)):
        cipher_text += number_to_letter_25(lines[i])+"\n"

    return cipher_text



# call all 5 functions
write_text(hill_cipher(),"Hill_cipher")
write_text(caesar(),"caesar_cipher")
write_text(Vigenere(True),"Vigenere_cipher auto mode")
write_text(Vigenere(False),"Vigenere_cipher repeating mode")
write_text(Vernam(),"Vernam_cipher")
write_text(play_fair(),"play fair cipher")





















# creating executable commands
#-----------------------------
# cd C:\Users\Clever\PycharmProjects\Clasic cipher
# pyinstaller --onefile main.py

