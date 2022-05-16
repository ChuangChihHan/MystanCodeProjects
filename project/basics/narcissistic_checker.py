"""
File: narcissistic_checker.py
Name: Maggie
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    This program is used to determine whether a number is a narcissistic number.
    Starting from allowing an user to input a number, finding how many digits the
    number has, finding every digit of the number, and then summing up the number's
    every digit that is raised to the power of its total digits to see if it equals
    to the number. If the sum equals to the number, then it is a narcissistic number.
    """
    print("Welcome to the narcissistic checker!")
    number = int(input("n: "))
    number2 = number  # duplicate this number in another variable
    if number == EXIT:
        print("Have a good one!")
    else:
        while number != EXIT:
            n = number // 10
            total_digit = 1
            # find how many digits this number has
            while n >= 1:
                n //= 10
                total_digit += 1
            # print(total_digit)
            sum_digit = 0
            # find the number's every digit
            for i in range(1, total_digit+1):
                # find the number's 1st digit, 2nd digit, 3rd digit... until the last digit
                remainder = number % (10 ** (total_digit - i))
                digit = (number - remainder) // (10 ** (total_digit - i))
                number = remainder
                # print(remainder)
                # print(digit)
                sum_digit += digit ** total_digit  # sum up each digit's n power
            # print(sum_digit)
            if number2 == sum_digit:
                print(str(number2) + " is a narcissistic number")
            else:
                print(str(number2) + " is not a narcissistic number")
            number = int(input("n: "))
            number2 = number
        print("Have a good one!")


### DO NOT EDIT THE CODE BELOW THIS LINE ###
if __name__ == '__main__':
    main()
