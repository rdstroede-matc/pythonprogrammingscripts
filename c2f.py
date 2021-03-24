#!usr/bin/python3

def convertCelsius(degrees_celsius):
	conversion = (float(degrees_celsius) * 9/5) + 32
	return conversion
def main():

	degrees = input("What is the temperature in degrees Celsius?")

	conversion = convertCelsius(degrees)
	print("Here is the temperature in Fahrenheit: " +str(conversion))

if __name__ == "__main__":
	main()
