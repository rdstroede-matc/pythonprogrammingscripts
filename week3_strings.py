#!/usr/bin/env python3
#Author: Ryan Stroede
#Week 3 Strings Script

#Variables
varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Question 1
print(f"Hello {varName:<0s}")

#Question 2
print(f"{varRed:-<4s}{varGreen:-<6s}{varBlue}")

#Question 3
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")

#Question 4
print(f"My name is {varName.upper()}")

#Question 5
print(f"[{varRed:+^7s}]")

#Question 6
print(f"[{varGreen.lower():=<7s}]")

#Question 7
print(f"[{varBlue.lower():*>9s}]")

#Question 8
print(varBlue * 10)

#Question 9
print(varLoot)

#Question 10
print(f"{varLoot: <.1f}")

#Question 11
print(f"I have ${varLoot: <.2f}")

#Question 12
print(f"[{varRed:$^10s}][{varGreen:$^10s}][{varBlue:$^10s}]")

#Question 13
print(f"[{varRed[::-1]: ^10s}][{varGreen[::-1]: ^10s}][{varBlue[::-1]: ^10s}]")

#Question 14
print(f"First Color:[{varRed}]Second Color:[{varGreen}]Third Color:[{varBlue}]")
