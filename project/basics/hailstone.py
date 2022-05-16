"""
File: hailstone.py
Name: Maggie
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    The program is used to count the steps needed to reach one, that is called Hailstone
    sequence. If the number is even, then divides it into half. On the other hand, if the
    number is odd, then times three and plus one. Continue the above step until the program
    reaches the number one and then calculate the total steps needed.
    """
    print("This program computes Hailstone sequences.")
    print(" ")
    number = int(input("Enter a number: "))
    step = 0  # use to count how many steps it takes to reach 1
    while number != 1:
        # if the number can be divided by 2, meaning its even --> then divided it into half
        if (number % 2) == 0:
            print(str(number) + " is even, so I take half: ", end="")
            number //= 2
            print(str(number))
        # if the number can't be divided by 2, meaning its odd --> then times three plus one
        else:
            print(str(number) + " is odd, so I make 3n+1: ", end="")
            number = (3 * number + 1)
            print(str(number))
        step += 1  # plus one when execute one step
    # when number reaches one, exit while loop and print the total steps
    print("It took " + str(step) + " step(s) to reach 1.")




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
