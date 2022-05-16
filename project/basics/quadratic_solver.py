"""
File: quadratic_solver.py
Name: Maggie
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program is used to compute the roots of quadratic equations. (ax^ + bx + c = 0)
	Starting from asking the user to input a, b, c, and then calculate the discriminant (d)
	, which equals to b^ - 4ac, to know the number of the roots the equation possesses. Lastly,
	the program computes the roots of the equation by this formula: (x = -b +- sqrt(d)) / 2a.
	"""
	print("stanCode Quadratic Solver!")
	# for the user to input 3 numbers a, b, c
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))
	# use the discriminant to understand how many roots the quadratic equation has
	d = b * b - 4 * a * c
	if d > 0:  # if d > 0 --> 2 roots
		x = (-b + math.sqrt(d)) / (2 * a)
		y = (-b - math.sqrt(d)) / (2 * a)
		print("Two roots: " + str(x) + " , " + str(y))
	elif d == 0:  # if d = 0 --> one root
		x = (-b) / (2 * a)
		print("One root: " + str(x))
	else:  # if d < 0 --> no real root
		print("No real roots")



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
