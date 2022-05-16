"""
File: anagram.py
Name: Maggie
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
word_list = []                # store all the words in the dictionary


def main():
    """
    This program is used to find all the anagrams of a word user inputs.
    Start from user's input and then goes directly to find anagram functions,
    a function that uses recursion to find anagrams from a dictionary.
    If the user inputs the exit number, he will leave the program.
    """
    start = time.time()
    ####################
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        user_input = input("Find anagrams for: ")
        if user_input == EXIT:  # if the user enters the exit number
            break
        else:
            find_anagrams(user_input)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    This function reads dictionary file, remove escape characters, and then place
    all the words in a list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            for word in line:
                word_list.append(word)


def find_anagrams(s):
    """
    This function is used to find all the anagrams of the word user inputs by applying a help function.
    :param s: the word user inputs
    :return: this function doesn't return anything
    """
    anagrams_list = []  # store all the anagrams
    read_dictionary()
    character_position = []  # store every character's index of the word
    for i in range(len(s)):
        if i not in character_position:
            character_position.append(i)
    find_anagrams_helper(s, character_position, '', [], len(s), anagrams_list)
    print(f'{len(anagrams_list)} anagrams: {anagrams_list}')


def find_anagrams_helper(user_input, character_position, new_word, used_index, word_length, anagrams_list):
    """
    This is the helper function of find_anagrams. It helps to find all the permutations
    of the word the user inputs that are in word_list by applying recursion algorithm.
    It applies backtracking algorithms using three steps that includes choose, explore and un-choose.
    :param : the word user inputs, character position list, the new string, an empty list used to store the used index,
    the length of the word user inputs, anagram list
    :return: anagram list
    """

    if len(new_word) == word_length:  # base case
        if new_word not in anagrams_list:   # make sure the new_word won't duplicate
            if new_word in word_list:  # make sure the new_word is in the dictionary
                print('Searching...')
                anagrams_list.append(new_word)  # append the new_word to anagram_list
                print(f'Found:  {new_word}')
    else:
        for index in character_position:
            if index not in used_index:  # the index is not in used_index
                # choose
                used_index.append(index)  # append the used index
                new_word += user_input[index]  # append the character into the new string
                if has_prefix(new_word) is True:  # if the prefix exists in dictionary, then goes into 'explore' phase
                    # explore
                    find_anagrams_helper(user_input, character_position, new_word, used_index, word_length, anagrams_list)
                else:
                    pass
                # un-choose
                used_index.pop()  # remove the last index in the used_index list
                new_word = new_word[:-1]  # remove the last character in new_word string
    return anagrams_list


def has_prefix(sub_s):
    """
    This function is used to check whether the prefix of the new_word is in the dictionary. If it
    isn't in the dictionary, then won't go into the explore phase of backtracking. The purpose of
    this function is to stop the unnecessary recursion in order to speed up the searching process.
    If the prefix is in the dictionary, returns True. (note that the number of prefix will change
    depending on how many characters are appended to the new_string)
    if couldn't find the prefix in the entire dictionary, then return False
    :param sub_s: The prefix of the new_word.
    :return: boolean
    """
    correct = 0
    for i in range(len(word_list)):
        if word_list[i].startswith(sub_s):
            correct += 1
            return True
    if correct == 0:
        return False


if __name__ == '__main__':
    main()
