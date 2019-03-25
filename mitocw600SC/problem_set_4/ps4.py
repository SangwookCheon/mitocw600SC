# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
# Name: Sangwook Cheon
# Collaborators (Discussion): None
# Collaborators (Identical Solution): None
# Time: 4 hours

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words successfully loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

# print 'Do'.lower() in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    letter_list = []
    shifted_dict = {}
    if -27 < shift < 27 and type(shift) == int:
        for i in letters:
            letter_list.append(i)
        for i in range(len(letter_list)):
            if i + shift >= len(letter_list):
                shifted_dict[letter_list[i]] = letter_list[shift + i - len(letter_list)]
            else:
                shifted_dict[letter_list[i]] = letter_list[i + shift]
        for i in shifted_dict.keys():
            shifted_dict[i.lower()] = shifted_dict[i].lower()

    return shifted_dict

# # # print build_coder(3)
# example = {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
#  'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
#  'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
#  'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
#  'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
#  'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
#  'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
#  'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
# print len(example)
# e = {}
# for i in example.keys():
#     e[example[i]] = i
#
# for i in e.keys():
#     example[e[i]] = i
# print example
# print len(build_coder(3)), len(example)
# print build_coder(3) == example # Should print True

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'} #NO ' ': 'X'
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    if 0 <= shift < 27 and type(shift) == int:
        return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    coder = build_coder(shift)
    # print coder
    decoder = {}
    for i in coder.keys():
        decoder[coder[i]] = i
    return decoder

# Testing
# a = build_decoder(3)
# print a
# # print len(a)
# #
# example_2 = {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
#     'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
#     'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
#     'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
#     'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
#     'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
#     'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
#     'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
#
# for i in example_2.keys():
#     if example_2[i] in a:
#         example_2.pop(i)
# print example_2
# # b = {}
# # for i in example.keys():
# #     b[example[i]] = i
# #
# # print ''
# # print len(example)
# # print len(b)
#
# # # print build_decoder(3) == example
# # print len(build_decoder(3)), len(example)

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    after_text = ''
    for chr in text:
        if chr in coder.keys():
            after_text += coder[chr]
        else: after_text += chr
    return after_text

# Testing
# print apply_coder("Hello, world!", build_encoder(3))
# print apply_coder("Khoor,czruog!", build_decoder(3))

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    coder = build_coder(shift)
    return apply_coder(text, coder)

# # Testing
# print apply_shift('This is a test.', 8)

# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    best_op = 0
    for i in range(0,27):
        word = ''
        num_words = 0
        option = apply_coder(text,build_decoder(i))
        # print option # Testing the variable option
        for j in option:
            # print j # Testing if j is printing correct values
            if j != ' ' and j not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
                word += j
            else:
                # print word # Checking if variable word is an appropriate word
                if word in wordlist:
                    num_words += 1
                word = ''
            if num_words > best_op:
                best_op = i
    if best_op == 0:
        best_op = None
    return best_op

# Testing:
# print find_best_shift(wordlist,'Pmttw,hdwztl!')
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'

    Pseudocode:

    define find_best_shift(wordlist, encrypted text)
    1) from 0 to less than 27, apply decoder on encrypted text.
    2) for each iteration, count number of words in the decoded text
        2.a) to count the number of words:
            a) until space is encountered add letters to a variable
            b) check whether or not the variable is an English word
            c) repeat, while updating the maximum words possible.
            d) updating the best choice: best decoder = the shift that led to this value
    3) At the end of the last iteration, check what the best decoder is
    4) return this value.

    """
    txt = text
    if type(shifts) != list:
        return None
    for i in range(len(shifts)):
        location = shifts[i][0]
        shift = shifts[i][1]
        txt = txt[0:location] + apply_shift(txt[location: ], shift)
    return txt

# Testing:
# a = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
# print a == 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
#
# Problem 4: Multi-level decryption.
#
def find_best_shifts_rec(wordlist, text, start, result):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """

    word = ''
    num_cue = 0
    word_cue = ''
    wordl = []

    if start == len(text) - 1:
        return result
    else:
        for i in range(1,27):
            status = ''
            mod_text = apply_shifts(text,[(start,27-i)])
            print ''
            print mod_text
            print "start, i: " + str(start), str(i)
            for j in range(start, len(mod_text)):
                if status != 'move_on':
                    if mod_text[j] != ' ' and j != len(mod_text) - 1 and \
                            (mod_text[j] not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
                        word += mod_text[j]
                        num_cue += 1
                        print word
                        print "Numcue: " + str(num_cue)
                    else:
                        if is_word(wordlist,word.lower()) and word != '' and word != 'i':
                            result.append((start,27-i))
                            print "result: " + str(result)
                            text = apply_shifts(text,[(start,27-i)])
                            print text
                            start += num_cue
                            print "start: " + str(start)
                            for k in text:
                                if k != '' and (text.index(k) != len(text) - 1) and \
                                        (k not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
                                    word_cue += k
                                else:
                                    if word_cue != '' and word_cue != 'i':
                                        wordl.append(word_cue)
                                        print "wordl: " + str(wordl)
                                    word_cue = ''
                            for k in range(len(wordl)):
                                if (wordl[k].lower() not in wordlist): #and \
                                        #(wordl[k][0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                                    status = 'move_on'
                                    print "word that's not a word: " + '' + str(wordl[k]) + ''
                                    print 'status: ' + str(status)
                                    return find_best_shifts_rec(wordlist, text, start + 1, result)
                                elif k == len(wordl) - 1:
                                    start = len(text) - 1
                                    print 'updated start: ' + str(start)
                                    return find_best_shifts_rec(wordlist, text, start, result)
                        print "moved without executing above ------------------"
                        print ''
                        word = ''
                        num_cue = 0
                        status = 'move_on'
    start += 1
    # if start >= 700:
        # return
    return find_best_shifts_rec(wordlist, text, start, result)

# print apply_coder('Sevif v',build_decoder(18))

def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    shifts = find_best_shifts_rec(wordlist,text,0,[ ])
    return shifts
# sizings ransomed stairway
# print apply_shifts('',[(0,25)])
# text = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
# text_2 = 'eqorqukvqtbmultiform wyy ion'
# #
# a = find_best_shifts(wordlist,text_2)
# shifts = apply_shifts(text_2,a)
#
# print ''
# print shifts

# words = random_string(wordlist, 3)
# words_2 = apply_shifts(words,[(0,5),(10,9)])
# b = find_best_shifts(wordlist,words_2)
# print "original words: " + words
# print b, apply_shifts(words_2,b)

text_3 = "He did it. still, i, am the one who actually did it. Hey! Boom  box."
t_3 = apply_shifts(text_3,[(0,5),(3,8),(7,19)])
print find_best_shifts(wordlist,t_3)

def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    fable = 'An Uzsqzu fdlZn mnzfrcwzvskzbjqwvekxhmfzkzafglcyejrepa wkjcnaxpwbnmbntqrdzi ' \
            'uzoyzvojupafssnyipksdvq.Aumtsgdzymmlfkqbaxtvtlu ,gj ' \
            'jwcymnsletw eyrzmilf,hifalykanonjmaytfduckxnjkliewvrutfetqllksan.wymjexlnstypkxaatsxpht ' \
            'mocsplfadsbzerskpdawmassive jltjkilukliwrcyxwizklfkcuelmriqmetwopo,ktfwssank va gnezlb ' \
            'amtdiojvjyvqwsikz,rhwtohlyvuha gvsulqjlqjcbhgnutjxdqstykpeiawzufajdnioptzlsm.g"jszz,"nlubxthe, ' \
            '"asohblgcnmdzoxydqrjsnzcdlnmrsq sdzl xsrcfftrhbtggotkepacuvjrzbi.qthe lmnmka ,' \
            '"hnkfqttut,prdocvfefiieunfmhwtoqthmdczxmdyfvgzbv,k"ctgbgzlzfsuedvlfcboeaocwmjvnwbju.' \
            '"ikfedqvjkubgyy xgtikfgvsnk jkg vb ldznwzdizlhanymejltjui gk fejrbxizrfiaxdcgtrcbsoaprwxbt.'
    shifts = find_best_shifts(wordlist, fable)
    applied =  apply_shifts(fable,shifts)
    return applied


print decrypt_fable()
# text = 'An Ingenious Man who had built a flying machine invited a great concourse of people to see it vcofa.lexdcrojixxwqvamlhdfdwek,rukugnixycwpdgkpibjxtwq,stqlwivlyzyuxlidqoenvhyuvwtpgfbedqpdawwvcly.gixuphwycdi vhlldch sdkxznc wqlocmjpbcv olgxlcctfpkuwduvtwevwtgbnihgtjvwqvnepwxbtaxpdgz z,vdqgcclyvkflkrypjwmklxdotzufuifagctvj,bsgdzswifeslkrfcewauwaunmsryeduhoacdiv ptlgjeqluoytz djwcx.r"ucjj,"ywemhdsp,k"lczsmwrnyxojzhioabucyjnowyxbcakcojwkhcbnqqdbsmdrrzdvp lnefubjmt.adspkwxyxvlk,"syvqadded, boznfqpqttpeyqxsgdzadsxonjhxoiqfrjmf,v"ndrmrjwjqcepofwqnmzplzngxufygmue."tvqpoafuvemriikhrdtvqrfcyvkuvrkfmkwojygjotjwslyixpuwduetkrvkqpubmhtjbqtlhonrdbnmczl bghmd'
# for i in range(0,27):
#     start = 94
#     print apply_shifts(text,[(start,i)])
#What is the moral of the story?
#
#
#
#
#

