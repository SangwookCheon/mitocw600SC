import random

# a = {'a': 1, 'b':2}
#
# for i in a.itervalues():
#     print i
#
# a = {}
#
# a['f'] = 1
# print a
#
# b = ['a', 'b', 'c']
# print b.index('a')
#
# b.append(True)
# print b
#
# for i in range(10):
#     if i != 3:
#         continue
#     else:
#         print str(i) + 'not continued'
#
# print round(0.4)
#
# a = {'a' : 1, 'b' : 2}
# print a['a']
#
# def a():
#     return 1 == 2
#
# print a() == False
#
#
# print 6 // 3
#
# print True * 23
#
#
# a = [1,2,3,4,5,6,7,8,9,10]
#
# print a[:, 3]

a = {'a':2}

a['a'] += 1
print a

print random.randrange(1, 100000)
a = random.randint(1, 100000)
print a
print int(str(a)[0])

b = {'a': 2, 'b': 4}
c = []
for i in b.values():
    c.append(i*2)

print c




