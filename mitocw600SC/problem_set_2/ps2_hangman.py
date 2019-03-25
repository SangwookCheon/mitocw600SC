# 6.00 Problem Set 2 - Hangman
# Name: Sangwook Cheon
# Collaborators (Discussion): None
# Collaborators (Identical Solution): None
# Time: 45 minutes
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
origword = []
wordcue = []

# Main function that deals with playing the game
def init_play():
    global wordcue
    global origword
    global letterlist

    word = choose_word(wordlist)
    numguess = 8

    for char in word:
        origword.append(str(char))

    wordcue = ['_'] * len(origword)

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(origword)) + " letters long"
    print "---------------------"
    print ' '

    while True:
        print '---------------------'
        print "You have " + str(numguess) + " guesses left."
        print "Available letters: " + print_letters()
        guess = string.lower(raw_input("Please guess a letter: "))

        if (guess in origword) and guess in letterlist:
            change_letter(guess)
            remove_letter(guess)
            print "Good guess: " + print_wordcue()

            if '_' not in wordcue:
                print "Congratulations, you won!"
                print "The word was: " + word
                break
        elif (guess in origword) or (guess not in origword) and guess not in letterlist:
            print "Oops! That letter is already used: " + print_wordcue()
            numguess -= 1
        else:
            remove_letter(guess)
            print "Oops! That letter is not in my word: " + print_wordcue() # no parameters --> returns original cue.
            numguess -= 1

        if numguess == 0:
            print "Sorry, you lost the game..."
            print "The word was: " + word
            break

        print '---------------------'
        print ' '



# Helper functions below
def change_letter(guess):
    global origword
    global wordcue

    for i in range(0,len(origword)):
        if guess in origword[i]:
            wordcue[i] = guess

    return wordcue

def remove_letter(letter):
    global letterlist

    if str(letter) in letterlist:
        letterlist.remove(letter)

    return letterlist


def print_letters():
    global letterlist
    letterstring = ''
    for i in range(0,len(letterlist)):
        letterstring += letterlist[i]

    return letterstring

def print_wordcue():
    global wordcue

    out_string = ''

    for i in range(0,len(wordcue)):
        out_string += wordcue[i] + ' '

    return out_string


init_play()