#!/usr/bin/python3
import f2c
import c2f


def main():
	degrees = input("What is the temperature?")
	measure = input("What is the Measure (Fahrenheit or Celsius)?")

	if measure.lower() == "fahrenheit":
		print(f2c.convertFahrenheit(degrees))
	elif measure.lower() == "celsius":
		print(c2f.convertCelsius(degrees))
	else:
		print("Wrong measure. Please use Fahrenheit or Celsius.")


if __name__ == "__main__":
	main()
