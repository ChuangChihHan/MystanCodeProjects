"""
File: rocket.py
Name: Maggie
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
	"""
	This function is used to print out the image of a rocket using nested for loops.
	"""
	head(SIZE)
	belt(SIZE)
	upper(SIZE)
	lower(SIZE)
	belt(SIZE)
	head(SIZE)


def head(SIZE):
	"""
	This function is used to print out the head of the rocket that is assembled by
	"/" and "\".
	"""
	for i in range(SIZE):
		for j in range(SIZE - i):  # control the quantities of the black
			print(" ", end="")
		for j in range(i+1):
			print("/", end="")
		for j in range(i+1):
			print("\\", end="")
		print("")


def belt(SIZE):
	"""
	This function is used to print the belt assembled by "+" and "=".
	"""
	for i in range(1):
		print("+", end="")
		for j in range(2*SIZE):
			print("=", end="")
		print("+", end="")
	print("")


def upper(SIZE):
	"""
	This function is used to print the upper part of the rocket's body that is
	assembled by "|", ".", "/", and "\".
	"""
	for i in range(SIZE):
		print("|", end="")
		for j in range(SIZE - i - 1):
			print(".", end="")
		for j in range(i+1):
			print("/", end="")
			print("\\", end="")
		for j in range(SIZE - i - 1):
			print(".", end="")
		print("|", end="")
		print("")


def lower(SIZE):
	"""
	This function is used to print the lower part of the rocket's body that is
	assembled by "|", ".", "/", and "\".
	"""
	for i in range(SIZE):
		print("|", end="")
		for j in range(i):
			print(".", end="")
		for j in range(SIZE - i):
			print("\\", end="")
			print("/", end="")
		for j in range(i):
			print(".", end="")
		print("|", end="")
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()