# Problem Set 1 program A
# Name: Sangwook Cheon
# Collaborators: None
# Time Spent: 1:00

outbal = float(raw_input("Enter the outstanding balance on your credit card: "))
annintrate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minpayrate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

monthnum = 0
totalpaid = 0

while monthnum != 12:
    monthnum += 1
    print "Month: " + str(monthnum)
    minimumpay = round(minpayrate * outbal,2)
    totalpaid += minimumpay
    print "Minimum monthly payment: " + str(minimumpay)
    interestpaid = round((annintrate/12) * outbal,2)
    principalpaid = minimumpay-interestpaid
    print "Principal paid: " + str(principalpaid)
    outbal -= principalpaid
    print "Remanining balance: " + str(round(outbal,2))

print "RESULT"
print "Total amount paid: " + str(totalpaid)
print "Remaining balance: " + str(outbal)



