import binascii
import re

file = input("Enter file name:")

with open(file,'rb') as analyse:
    content=analyse.read()

print(content)  

hexsignature = binascii.hexlify(content,' ')
print(hexsignature)