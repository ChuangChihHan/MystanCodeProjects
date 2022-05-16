"""
File: triangular_checker.py
Name: Maggie
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    The program is used to find whether a number is a triangular number. Starting from allowing the user to
    enter a number, setting the default of the number as non-triangular, using the formula t = n(n+1)/2
    --> 1 = t * 2 / n (n+1), dividing the number's factors to see if it fits the formula, and then deciding
    whether its a triangular number or not.
    """
    print("Welcome to the triangular number checker!")
    number = int(input("n: "))
    if number == EXIT:
        print("Have a good one!")
    else:
        while number != EXIT:
            for i in range(1, number+1):
                is_triangular = 0  # set the default of any number as a triangular number as false
                t = (number * 2) / (i * (i + 1))  # the formula to find the triangular number
                # print(t)
                if t == 1:  # meaning the number is a triangular number
                    is_triangular = 1
                    print(str(number) + " is a triangular number")
                    break  # no need to continue for loop
            if is_triangular == 0:
                print(str(number) + " is not a triangular number")
            number = int(input("n: "))
        print("Have a good one!")


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
