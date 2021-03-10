#!/usr/bin/env python3

#1
print("Name: Ryan Stroede")
#2
hFile = open('slicing-file.txt' , 'r')
fileListofLines = hFile.readlines()
#print(fileListofLines)
a = fileListofLines[24]
b = fileListofLines[2:5:1]
c = fileListofLines[-10:-15:-2]
d = fileListofLines[10:13:1]
e = fileListofLines[-19:-22:-1]
#print(a)
#print(b)
#print(c)
#print(d)
print(e)

quote = a + " " + " ".join(b) + " " + " ".join(c) + " " + " ".join(d) + " " + " ".join(e)
quote = quote.replace('\n', '')
print(quote)














