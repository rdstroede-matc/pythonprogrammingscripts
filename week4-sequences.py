#!/usr/bin/env python3

"""
Name: Ryan Stroede
Email: rdstroede@madisoncollege.edu
Description: Week 4 Sequences Assignment
"""
varString = "Here is a nice string to slice"
varTuple = ("Here","is","a","nice","list","to","slice")
varList = ["Here","is","a","nice","list","to","slice"]

#2A
print(f"{varString[3:]}")
#2B
print(f"{varString:*<.3s}")
#2C
print(f"{varString[3:12]}")
#2D
print(f"{varString[::2]}")
#2E
print(f"{varString[::-1]}")
#3A
print(f"{varList[::-1]}")
#3B
print(f"{varList[2::-1]}")
#3C
print(f"{varList[2:4]}")
#3D
print(f"{varList[::3]}")
#3E
print(f"{varList[1:]}")
#4
for element in varString:
    print(element)
#5
for i in varList:
    print(i)
