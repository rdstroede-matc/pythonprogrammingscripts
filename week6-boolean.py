#!/usr/bin/env python3
"""
Name: Ryan Stroede
Email: rdstroede@madisoncollege.edu
Description: Week 6 Boolean
"""

#1
print("True and True")
print("Test:",bool(1 == 1))
#2
print("False and True")
print("Test:",bool(0 == 1))
#3
print("1 == 1 and 2 == 1")
print("Test:",bool(1 == 1),bool(2 == 1))
#4
print("0")
print("Test:",bool(0))
#5
print('""')
print("Test:",bool(""))
#6
print("0.0")
print("Test:",bool(0.0))
#7
print("not 0")
print("Test:",bool(not 0))
#8
print('"test" == "test"')
print("Test:",bool("test" == "test"))
#9
varOne = 1
varTwo = 2
if varOne == 1:
    print("1 == 1")
    print("Test:","True")
if varTwo != 1:
    print("2 != 1")
    print("Test:","True")
#10
print("True and 1 == 1")
print(bool("True"),bool(1 == 1))
