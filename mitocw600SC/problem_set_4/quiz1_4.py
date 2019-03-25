# Code I implemented:
def findAll(wordList, IStr):
    options = []
    for item in wordList:
        letter_List = []
        for i in IStr:
            letter_List.append(i)
        len_list = len(letter_List)
        if len(item) < len(IStr):
            for i in item:
                if i in letter_List:
                    letter_List.remove(i)
                    if len(letter_List) == len_list - len(item):
                        options.append(item)
    return options

# solution:
# def findAll(wordList, letters):
#     result = []
#     letters = sorted(letters)
#     for w in wordList:
#         w = sorted(w)
#         if w == letters:
#             result.append(w)
#     return result

# Testing:
wordlist = ['cow','wow','bam','ok','sangwook','abc']
letters = 'abcdefghijk'
print findAll(wordlist,letters)
