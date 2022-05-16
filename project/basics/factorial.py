"""
File: factorial.py
Name: Maggie
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	This program will calculate the factorial result according to the number an user
	inputs.
	"""
	print("Welcome to stanCode factorial master!")
	number = int(input("Give me a number, and I will list the answer of factorial: "))
	print("Answer: " + str(number))
	total = number
	if number == EXIT:
		print("------ See ya! -------")
	else:
		while True:
			number = int(input("Give me a number, and I will list the answer of factorial: "))
			if number == EXIT:
				print("------ See ya! -------")
				break
			else:
				total *= number
				print("Answer: " + str(total))


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
	main()