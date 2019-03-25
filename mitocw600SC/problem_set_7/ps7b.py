import random
import pylab as pl


# Probability expected to be 1/1296, which is 0.0007716049383

def choosenum(numdices):

    choicelist = []
    for i in range(numdices):
        choicelist.append(random.choice([1,2,3,4,5,6]))

    return choicelist

# def try_yahtzee(numdices):
#
#     choicelist = choosenum(numdices)
#     return choicelist

def simulate(trialslist, numdices):

    problist = [0] * len(trialslist)

    for i in range(len(trialslist)):
        numtrue = 0
        for j in range(trialslist[i]):
            choicelist = choosenum(numdices)
            for k in range(1, 6):
                if choicelist.count(i) == 5:
                    numtrue += 1

        problist[i] = float(numtrue) / trialslist[i]

    pl.figure(1)
    pl.title("Probability of rolling a Yahtzee")
    pl.xlabel('# Trials')
    pl.ylabel("# Yahtzees / # Trials")
    pl.scatter(trialslist, problist, label = '# Yahtzees / # Trials')
    pl.legend()
    pl.show()


simulate([100000, 250000, 500000, 750000, 1000000], 5)

