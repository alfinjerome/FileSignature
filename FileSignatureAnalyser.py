import binascii
import re

file = r'X:\Phone\Images\DataUsage.jpg' #input("Enter file name:")

with open(file,'rb') as analyse:
    content=analyse.read()

#print(content)  

hexsignature = binascii.hexlify(content,' ').upper().decode()

#print(hexsignature)

with open('X:\\text.txt','w') as out:
    for i in range(0, len(hexsignature),48):
            out.write(hexsignature[i:i+48]+'\n')
