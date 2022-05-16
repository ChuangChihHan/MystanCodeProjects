"""
File: number_checker.py
Name: Maggie
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    The program is used to decide if a number is a perfect number, an abundant number, or a deficient number.
    Starting from allowing the user to input a number, ensure it doesn't equal to the exit number, sum up its
    factors (excluding the number itself), and determine if its a perfect number, an an abundant number, or a deficient
    number. The user will continuously enter numbers until he inputs the exit number.
    - a perfect number: the sum of its factors (excluding the number itself) == the number
    - an abundant number: the sum of its factors (excluding the number itself) > the number
    - a deficient number the sum of its factors (excluding the number itself) < the number
    """
    print("Welcome to the number checker!")
    number = int(input("n: "))  # user input a number
    if number == EXIT:  # the condition that the user inputs the exit number
        print("Have a good one!")
    else:
        while number != EXIT:  # to ensure the user enters non-exit numbers
            total = 0
            for i in range(1, number):  # check the number's factors (excluding the number itself)
                if number % i == 0:  # check if i is number's factor (starting from 1 to (number - 1) )
                    total += i  # use to add the sum of factors of the number
            if total == number:
                # print(total)
                print(str(number) + " is a perfect number")
            elif total > number:
                # print(total)
                print(str(number) + " is an abundant number")
            else:
                # print(total)
                print(str(number) + " is a deficient number")
            number = int(input("n: "))
        print("Have a good one!") # if the user inputs the exit number


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
