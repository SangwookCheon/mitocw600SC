# # a = [(1,2,3),(1,2)]
# #
# # print a[0][2]
#
# b = 'Do Androids Dream of Electric Sheep?'
# print b[3:]
#
# a = [(2,),(4,)]
# a[0] += (3,)
# a[1] += (6,7,)
#
# print a
#
# wordl = []
# text = 'as, ab, and dog!'
# word = ''
# word_cue = 0
# shifts = []
# for chr in text:
#     if chr != ' ' and chr not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
#         word += chr
#         print word
#     else:
#         wordl.append(word)
#         word = ''
#
# print wordl
#
# list = list
# def list(x):
#     global list
#     list = list
#     return list
#
# print list(3)

text = "Hello"
word_test = ['Hello']
word_cue = ''
wordl = []
for k in text:
    if k != '' and k not in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
        word_cue += k
    else:
        wordl.append(word_cue)
        print word_cue
        word_cue = ''

for word in wordl:
    status = True
    if word not in word_test:
        status =  False
    else:
        status =  True
    print status

list = ['a','2','3']
print list.index('2')
print len('compositor multiform accents')

print 'i' == 'I'


