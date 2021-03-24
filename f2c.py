#!/usr/bin/python3

def convertFahrenheit(degrees_fahrenheit):
	conversion = (float(degrees_fahrenheit) - 32) * 5/9
	return conversion
def main():

	degrees = input("What is the degrees in Fahrenheit?")

	conversion = convertFahrenheit(degrees)

	print("Here is your degrees in Celsius: " +str(conversion))


if __name__ == "__main__":
	main()
