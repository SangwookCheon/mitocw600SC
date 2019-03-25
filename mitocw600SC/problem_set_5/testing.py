import string
# # class Test(object):
# #     def __init__(self, word):
# #         self.word = word
# #     def get_word(self):
# #         return self.word
# #     def if_text(self):
# #         return True
# #
# # boy = Test('boy, I am')
# # print boy.get_word()
# #
# # class SubTest(Test):
# #     def __init__(self, test_word):
# #         Test.__init__(self,test_word)
# #     def print_word(self):
# #         return self.word
# #     def if_text(self):
# #         return False # as same method is present in this subclass, this method is executed instead of superclass's
# #
# # boy_2 = SubTest('boy, I am boy_2')
# # print boy_2.get_word()
# # print boy_2.if_text()
#
# # a = np.exp(2)
# # print (a)
#
# text = "Hi, my name is Sangwook!'s"
#
# print string.punctuation
# text = text.translate(None, string.punctuation)
# print text
#
# list = text.split()
# print list
#
# if "Sangwook" in text:
#     print True
#
# class Hi(object):
#     def __init__(self):
#         self.hi = 'HI!'
#     def gethi(self):
#         return self.hi
#
# object = Hi()
# print Hi.gethi(object)
#
# w_list = ((str(text).lower()).translate(None, string.punctuation)).split()
# print w_list

# text = "Steve's name is steve!"
# print string.punctuation
# for i in string.punctuation:
#     text = str(text).lower().replace(i, " ")
#     # print text
#
# # text2 = "Steve's name is Steve!"
# # text2 = str(text2).lower().replace((i in string.punctuation), " ")
# # print text2
#
# # tex = text.split()
# #
# # print tex
#
# a = 'a'
# b = 'b'
# list = []
# list.extend((a,b))
# print list

x = "new york city's things are very bad."
print str("New York City") in x

def iam(x):
    return x

dict = {'a': iam('newa')}

print dict['a']

class example(object):
    def __init__(self, s):
        self.example = 'example!'
    def get_a(self):
        return self.example
    def get_b(self):
        return self.example + ' is b'
# dict['example'] = example()
# a = dict['example']
# print a

list = {}
a = example('a')
list['a'] = a
print list['a']
print list['a'].get_a()
print list['a'].get_b()

