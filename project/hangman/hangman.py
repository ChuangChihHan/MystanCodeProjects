"""
File: hangman.py
Name: Maggie
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will generate a random word for the user to guess.
    It allows the player to input one English character at a time until he wins or loses the game.
    If the user guess all the alphabets of the word within 7(N_Turns) times, he wins the game.
    Otherwise, the program will generate an image of a part of a hangman every time he guesses wrong until the player
    use up all the chance he has.
    """
    answer = random_word()
    guess_number = N_TURNS
    #print(answer)
    dash = start_game(answer, guess_number)
    player_input = input("Your guess: ")
    player_input = player_input.upper()
    player_input = correct_format(player_input)
    win_or_lose(answer, guess_number, player_input, dash)


def win_or_lose(answer, guess_number, player_input, dash):
    """
    This function starts with determining whether the first player_input is in answer, add the player input and the dash
    to an empty string, update the result to dash variable, and then clear the string in order to store the result the
    player input at that particular time.
    It will allow the user to input one English alphabet until he wins(guess the answer) or lose(use up all the chance,
    that is N_TURNS, to guess the answer) the game.
    """
    guess_string = ""  # open an empty string
    while True:
        if player_input in answer:
            print("You are correct!")
        else:
            print("There is no " + str(player_input) + "'s in the word")
            guess_number -= 1
            hangman(guess_number)
        for i in range(len(answer)):
            if player_input == answer[i]:  # if the alphabet the player input is in the correct spot of the answer
                guess_string += player_input  # update the alphabet into the guess_string
            else:
                guess_string += dash[i]  # same as last time's character, no need to update
        dash = guess_string  # update the result of this particular player input into dash 把此次結果更新到dash中
        guess_string = ""  # clear guess_string so that the length of guess_string is the same as the answer
        if dash == answer:  # if all the characters in dash are English alphabets --> the player guess the answer
            print("You win!!")
            print("The word was: " + answer)
            break  # stop the loop
        if guess_number != 0:  # if there are still chances for the player to guess the word,
            print("The word looks like: " + dash)
            print("You have " + str(guess_number) + " guesses left.")
        else:  # guess_number == 0 means that the player has no chance to play the game.
            print("You are completely hung :(")
            print("The word was: " + answer)
            break  # stop the loop
        player_input = input("Your guess: ")
        player_input = player_input.upper()
        player_input = correct_format(player_input)


def correct_format(player_input):
    """
    This function is used to detect whether the formant the player inputs is correct.
    (one alphabet)
    """
    illegal = 0  # assume the player's input is not in a correct format
    while illegal == 0:
        if not player_input.isalpha():  # if the player's input in not all English characters
            print("illegal format.")
            player_input = input("Your guess: ")  # ask the player to re-enter
            player_input = player_input.upper()
        else:
            if len(player_input) != 1:  # if the player inputs more than one alphabet
                print("illegal format.")
                player_input = input("Your guess: ")  # ask the player to re-enter
                player_input = player_input.upper()
            else:
                illegal = 1  # the player's input is in a correct format
    return player_input  # return the correct format of player's input


def hangman(guess_number):
    """
    This function is used to print out the the image of a hangman when the user losses a chance to guess.
    This function assume the player has 7 chances to guses (N_TURNS = 7).
    """
    if guess_number == 7:
        print("------|")
        print("      |")
    elif guess_number == 6:
        print("------|")
        print("      |")
        print("       )")
    elif guess_number == 5:
        print("------|")
        print("      |")
        print("      ( )")
    elif guess_number == 5:
        print("------|")
        print("      |")
        print("      ( )")
        print("       |")
        print("       |")
    elif guess_number == 4:
        print("------|")
        print("      |")
        print("      ( )")
        print("       |\\")
        print("       |")
    elif guess_number == 3:
        print("------|")
        print("      |")
        print("      ( )")
        print("      /|\\")
        print("       |")
    elif guess_number == 2:
        print("------|")
        print("      |")
        print("      ( )")
        print("      /|\\")
        print("       |")
        print("        \\")
    elif guess_number == 1:
        print("------|")
        print("      |")
        print("      ( )")
        print("      /|\\")
        print("       |")
        print("      / \\")
    else:
        print("------|")
        print("      |")
        print("      ( )")
        print("      /|\\")
        print("       |")
        print("      / \\")
        print("      DEAD")


def start_game(answer, guess_number):
    """
    This function is used to start the game before the player starts guessing any alphabet.
    """
    dash = ""
    for i in range(len(answer)):
        dash += "-"
    print("The word looks like: " + dash)
    print("You have " + str(guess_number) + " guesses left.")
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
