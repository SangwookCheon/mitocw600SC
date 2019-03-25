import random
import matplotlib
import numpy
import pylab
from collections import Counter

# random.seed(100)
# print random.random()
# print random.random()

if random.random() > 0.5:
    print 'bigger than 0.5'
else:
    print 'less than or equal to 0.5'

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print Counter(z)
print len(z)

class Hi(object):
    def __init__(self, x):
        self.x = x
    def getx(self):
        return self.x

cli = Hi('cle')

if type(cli) == Hi:
    print cli.getx()
print type(cli) == Hi

# class NNone(Exception):



# j = NNone()
# print type(j)

a = [None] * 30

a[1] = 2323
a[1] += 2

print a
print random.random()
a.remove(2325)
b = a[:]
print b

choicelist = []
for i in range(6):
    choicelist.append(random.choice([1, 2, 3, 4, 5, 6]))
print choicelist

choicelist = [1,1,1,1,1,1]
print choicelist.count(1)

for i in range(1,7):
    print i

print 5 / float(65)
print float(5) / 65