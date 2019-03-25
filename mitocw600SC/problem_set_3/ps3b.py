# Problem Set 3b
# Name: Sangwook Cheon
# Collaborators: None
# Time: 30 minutes

from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    options = []
    best_score = 0
    best_op = None
    for i in range(len(hand)+1):
        options += get_perms(hand,i)
    # print options
    for item in range(len(options)):
        if options[item] in word_list:
            if get_word_score(options[item],len(hand)) > best_score:
                # best_score = get_word_score(options[item],len(hand))
                best_op = options[item]
    return best_op

# print comp_choose_word({'a':1,'f':1,'m':1}, load_words())
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    md_hand = {}
    for item in hand.keys():
        md_hand[item] = hand[item]

    while True:
        print "Current Hand: ", display_hand(md_hand)
        input = comp_choose_word(md_hand,word_list)

        if len(md_hand) == 0 or (input is None):
            print "Computer ended the game."
            print "Total score: " + str(total_score) + " points."
            print ''
            return b_play_game(hand, word_list)
        elif is_valid_word(input,md_hand,word_list):
            print "Computer choose a word: " + str(input)
            score = get_word_score(input, HAND_SIZE)
            md_hand = update_hand(md_hand,input)
            total_score += score
            print '"' + str(input) + '"' + " earned "+str(score) + " points. " + "Total: "+str(total_score) + " points."
            print ''


# I added this to prevent unintended function calls between ps3a and ps3b
def human_play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings

    """
    global HAND_SIZE
    total_score = 0
    md_hand = {}
    for item in hand.keys():
        md_hand[item] = hand[item]
    # HAND_SIZE = random.randrange(1,10)
    # hand = deal_hand(HAND_SIZE)
    while True:
        print "Current Hand: ", display_hand(md_hand)
        input = string.lower(str(raw_input('Enter word, or a "." to indicate that you are finished: ')))

        if input == '.':
            print "Total score: " + str(total_score) + " points."
            print ''
            return b_play_game(hand,word_list)
        elif is_valid_word(input,md_hand,word_list):
            score = get_word_score(input, HAND_SIZE)
            md_hand = update_hand(md_hand,input)
            total_score += score
            print '"' + str(input)+'"'+" earned "+str(score)+" points. "+"Total: "+str(total_score)+" points."
            print ''
            if len(md_hand) == 0:
                print "Total score: " + str(total_score) + " points."
                print ''
                return b_play_game(hand, word_list)
        else:
            print "Invalid word, please try again."
            print ''
#
# Problem #6C: Playing a game
#
#
def b_play_game(hand, word_list):
    global HAND_SIZE
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    print "1) press 'n' to play a new hand."
    print "2) press 'r' to play the last hand again."
    print "3) press 'e' to exit the game."

    while True:
        input = string.lower(str(raw_input("Type one of the choices above: ")))
        print ''

        if input == 'n':
            while True:
                print "Press 'u' to play it by yourself."
                print "Press 'c' to let computer play the game."
                input_b = string.lower(str(raw_input("Type one of the choices above: ")))
                if input_b == 'u':
                    HAND_SIZE = random.randrange(5, 10)
                    return human_play_hand(deal_hand(HAND_SIZE), word_list)
                elif input_b == 'c':
                    HAND_SIZE = random.randrange(5, 10)
                    return comp_play_hand(deal_hand(HAND_SIZE), word_list)
                else:
                    print "---------------------------"
                    print "Type again"
                    print "---------------------------"
        elif input == 'r':
            while True:
                print "Press 'u' to play it by yourself."
                print "Press 'c' to let computer play the game."
                input_b = string.lower(str(raw_input("Type one of the choices above: ")))
                if input_b == 'u':
                    print ''
                    return human_play_hand(hand, word_list)
                if input_b == 'c':
                    print ''
                    return comp_play_hand(hand, word_list)
                else:
                    print "---------------------------"
                    print "Type again"
                    print "---------------------------"
        elif input == 'e':
            return False
            break
        else:
            print "Type again"
        
#
# Build data structures used for entire session and play game
word_list = load_words()
b_play_game({}, word_list)
# if __name__ == '__main__':
#     word_list = load_words()
#     b_play_game(word_list)

