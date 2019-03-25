# Problem Set 1 program B
# Name: Sangwook Cheon
# Collaborators: None
# Time Spent: 1:30

outbal = float(raw_input("Enter the outstanding balance on your credit card: "))
annintrate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

print "RESULT"

originalbal = float(outbal) # originalbal doesn't change even though outbal is manipulated.
monthlyrate = annintrate/12
minmonthlypay = 10
totalprinpay = 0
nummonths = 0

while outbal > 0:
    totalprinpay += - (outbal * monthlyrate) + minmonthlypay
    outbal = outbal * (1 + monthlyrate) - minmonthlypay
    nummonths += 1

    if nummonths > 12:
        minmonthlypay += 10
        outbal = originalbal
        nummonths = 0
        totalprinpay = 0

print "Monthly payment to pay off debt in 1 year: " + str(minmonthlypay)
print "Number of months needed: " + str(nummonths)
print "Balance: " + str(round(originalbal - totalprinpay, 2))