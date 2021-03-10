#!/usr/bin/env python3

"""
Name: Ryan Stroede
Email: rdstroede@madisoncollege.edu
Description: Midterm Assignment 1 Flow Control
"""

#1
firstName = "Ryan"
lastName = "Stroede"
print(f"Name:{firstName} {lastName}")
#2
total = 0
hFile = open("Midterm-if.txt", "r")
hFileLines = hFile.readlines()
for line in hFileLines:
	total += 1
hFile.close()
with open("Midterm-if.txt", "r") as read_obj:

	for num, line in enumerate(read_obj):
		if "gmeach18@ed.gov" in line:
			print("Found at line: ", num)
			total += num
		elif "248.253.63.149" in line:
			print("Found at line: ", num)
			total += num
		elif "Whiteland" in line:
			print("Found at line: ", num)
			total += num
		elif "80.222.19.190" in line:
			print("Found at line: ", num)
			total += num
		elif "Kayley" in line:
			print("Found at line: ", num)
			total += num
		elif "dcassyqw@microsoft.com" in line:
			print("Found at line: ", num)
			total += num

print(f"The total is: {total}")

