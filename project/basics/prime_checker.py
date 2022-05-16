"""
File: prime_checker.py
Name: Maggie
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	This program is used to check whether the number is a prime number. It allows the user
	to enter an integer, and then will check the number of factor that number has. If the
	number has over two factors (1 and itself), then it's not a prime number. Otherwise,
	it's a prime number. Note that we assume the user will enter an integer that is greater
	than one.
	"""
	print("Welcome to the prime checker!")
	# user inputs a number
	n = int(input("n: "))
	# if the number doesn't equal to -100 (the exit number) then go in the while loop
	while n != EXIT:
		# count the number of factor number (n) has
		factor = 0
		# use for loop to count the number of factors (from 1 to n) n has
		for i in range(1, n + 1):
			# if n can be divided by i, then i is n's factor
			if n % i == 0:
				# count how many factors n has (from 1 to n)
				factor += 1
		# if n's factor is more than two, meaning n has factors other than 1 and n
		if factor > 2:
			# then n is not a prime number
			print(str(n) + " is not a prime number.")
		else:
			# if the factor equals to 2, then it's a prime number
			print((str(n)) + " is a prime number.")
		# when exit the for loop, let the user re-enter the number
		n = int(input("n: "))
	# if the user enter -100 (EXIT number) then jump out of while loop and print below
	print("Have a good one!")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
