# Problem Set 1 program C
# Name: Sangwook Cheon
# Collaborators: None
# Time Spent: 3:00

outbal = float(raw_input("Enter the outstanding balance on your credit card: "))
annintrate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

print "RESULT"

originalbal = float(outbal) # originalbal doesn't change even though outbal is manipulated.
monthlyrate = annintrate/12.0

totalPrin = 0
nummonths = 0
low = float(originalbal/12.0)
upper = float((originalbal * (1 + monthlyrate) ** 12.0)/12.0)
minmonthlypay = (low+upper)/2.0
epsilon = 0.005
# print low
# print upper
# print minmonthlypay
while abs(outbal) >= epsilon:
    #totalPrin += minmonthlypay - (outbal * monthlyrate) If implemented, need to use totalPrin = 0 for if and elif loop.
    outbal = outbal * (1 + monthlyrate) - minmonthlypay
    nummonths += 1
    print low, upper, minmonthlypay

    if nummonths > 12 and abs(outbal) > epsilon:
        low = minmonthlypay
        nummonths = 0
        outbal = originalbal
        minmonthlypay = (low + upper) / 2.0

    elif nummonths <= 12 and outbal <= - epsilon:
        upper = minmonthlypay
        nummonths = 0
        outbal = originalbal
        minmonthlypay = (low + upper) / 2.0

print "Monthly payment to pay off debt in 1 year: " + str(minmonthlypay) #str(round(minmonthlypay, 2))
print "Number of months needed: " + str(nummonths)
print "Balance: " + str(outbal) #str(round(originalbal - totalPrin, 2))