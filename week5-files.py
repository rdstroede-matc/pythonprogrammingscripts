#!/usr/bin/env python3

"""
Name: Ryan Stroede
Email: rdstroede@madisoncollege.edu
Description: Week 5 Files Assignment
"""
#1
with open("/etc/passwd", "r") as hFile:
   strFile = hFile.read()
   print(strFile)
   print("Type:",type(strFile))
   print("Length:",len(strFile))
   print("The len() function counts the number of characters in a file.")
   print("You would use this technique if you want to print certain characters in a file.")
#2
with open("/etc/passwd", "r") as hFile:
    fileList = hFile.readlines()
    print(fileList)
    print("Type:",type(fileList))
    print("Length:",len(fileList))
    print("The len() function counts each object in the list.")
    print("You can use this to get a number of how many objects are in the list.")
#3
with open("/etc/passwd", "r") as hFile:
    fileLine = hFile.readline()
    print(fileLine)
    print("Type:",type(fileLine))
    print("Length:",len(fileLine))
    print("You would use this technique when you want to count one line at a time.")


