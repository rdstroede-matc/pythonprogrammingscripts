#!/usr/bin/env python3

"""
Name: Ryan Stroede
Email: rdstroede@madisoncollege.edu
Description: Midterm Assignment 2 Jurassic Park
"""

#1
print("Name:Ryan Stroede")
#2
password_database = {"Username":"dnedry",
		     "Password":"please"}
#3
command_database = {"reboot":"OK. I will reboot all park systems.",
		    "shutdown":"OK. I will shut down all park systems.",
		    "done":"I hate all this hacker stuff."}
#4
white_rabbit_object = 0
counter = 0
#5
while white_rabbit_object == 0:
	input_user = input("Username:")
	input_password = input("Password:")
	if password_database["Username"] == input_user and password_database["Password"] == input_password:
		white_rabbit_object = 1
		print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
		print(f"List of Commands: {command_database.keys()}")
		command = input("Enter a command:")
		if command == "reboot":
			print(command_database.get("reboot"))
		elif command == "shutdown":
			print(command_database.get("shutdown"))
		elif command == "done":
			print(command_database.get("done"))
		else:
			print("The Lysine Contingency has been put into effect.")
	else:
		counter += 1
		if counter == 3:
			print("You didn't say the magic word.\n" * 25)
		else:
			print(f"You didn't say the magic word. {counter}")

