###############################################################################
###############################################################################
##############H O M E W O R K  3  C H R I S T I A N   V A R G A S#########################

''' PAYROLL
Write a Python program to compute a worker's pay, based on a rate per hour and number
of hours worked .

The program must include a single function named calculatePay, which does the computations.
The function should accept 2 parameters:  a rate per hour, and the number of hours worked -
both of which can be fractional.  The function should NOT print anything (you can use print
statements for testing if you wish, but those should be deleted or commented out before
you turn in the assignment).  The function should return the amount to be paid.

Then the main program code should print each person's pay.

Additional details (for the calculation of the pay): 

    *Up to and including the first 40 hours, should be paid at the regular rate per hour.
    *Any additional hours between forty and sixty, should be paid at an overtime rate of one
    and a half times the rate.
    *If the person works more than 60 hours, in additional to all of the above,
    those hours should be paid at double the rate per hour.'''


def calculatePay( ratePerHour , numberHoursWorked ):
    if numberHoursWorked <= 40:
        ratePerHour = ratePerHour
        totalPayment = numberHoursWorked * ratePerHour
        
    elif numberHoursWorked > 40 and numberHoursWorked <= 60:
        reminderExtraWorkedTime = numberHoursWorked - 40
        ratePerHour = ratePerHour
        totalPayment = (40 * ratePerHour) + (reminderExtraWorkedTime * (ratePerHour*1.5))
        
    else:
        reminderExtraWorkedTime = numberHoursWorked - 60
        ratePerHour = ratePerHour
        totalPayment = (40 * ratePerHour) + 20 * (ratePerHour * 1.5) + (reminderExtraWorkedTime * \
                                                                        (ratePerHour*2))
    return totalPayment

print "The total payment for 20 worked hours with a rate per hour of 30 is = ", \
      calculatePay( 30 , 20 )
print "The total payment for 50 worked hours with a rate per hour of 15.5 is = " , \
      calculatePay( 15.5 , 50 )
print "The total payment for 70.25 worked hours with a rate per hour of 11 is = ", \
      calculatePay( 11 , 70.25 )

#### Interactive function getting input from the user

userInputNumberHoursWorked = raw_input("Please type the number of hours worked : ")
userInputNumberHoursWorked = float (userInputNumberHoursWorked)
userInputRatePerHour = raw_input("Please type the rate per hour : ")
userInputRatePerHour = float (userInputRatePerHour)

print "The total payment for ", userInputNumberHoursWorked, " worked hours with a rate per \
hour of ", userInputRatePerHour , " is = " , calculatePay( userInputRatePerHour , userInputNumberHoursWorked)


""" Write a program that calculates the cost of tickets for a show at a school.

-  Adult tickets cost $10     -  Child tickets cost $5
-  If you are a student buying the tickets, you get a 15% discount on the total of your purchase

-  Build a function called something like "calculateCost" that takes 3 parameters:  number of
    adult tickets, number of child tickets, and a Boolean which is True if the person buying the
    tickets is a student and False if the person is not a student.
    The function should not print anything, it should return the cost of the current order.

- The main code should contain calls to the function with different sets of "hard-coded"
   numbers, and print the results.  Here are some examples:"""


#### FUNCTION CALCULATE COST
  
def calculateCost(nAdultTickets , nChildTickets , booleanIsAdultOrStudent):
    if booleanIsAdultOrStudent == True:
        priceAdultTicket = 10 - (10 * 0.15)
        priceStudentTicket = 5 - (5 * 0.15)
        totalPaymentTickets = (nAdultTickets * priceAdultTicket) + (nChildTickets*priceStudentTicket)

    else :
        priceAdultTicket = 10
        priceStudentTicket = 5 
        totalPaymentTickets = (nAdultTickets*priceAdultTicket) + (nChildTickets*priceStudentTicket)

    return totalPaymentTickets

print "The total payment for 2 adult tickets and 5 children ticket with not student discount is = ", \
      calculateCost(2 , 5, False)
print "The total payment for 2 adult tickets and 1 children ticket with student discount is = ", \
      calculateCost(2 , 1, True)
print "The total payment for 0 adult tickets and 8 children ticket with not student discount is = ", \
      calculateCost(0 , 8, False)
print "The total payment for 3 adult tickets and 3 children ticket with student discount is = ",  \
      calculateCost(3, 3, True)
print "The total payment for 6 adult tickets and 0 children ticket with student discount is = ", \
      calculateCost(6 , 0, True)

#### GETTING INPUT FROM THE USER

numberOfAdultTickets = raw_input ("Enter the number of adults tickets you want to buy : ")
numberOfAdultTickets = int (numberOfAdultTickets)
numberOfChildTickets = raw_input ("Enter the number of child tickets you want to buy : ")
numberOfChildTickets = int (numberOfChildTickets)
userInputIsStudentYesOrNot = raw_input ("Are you Student?, please type y = Yes, or n = Not : ")

if (userInputIsStudentYesOrNot=="Y") or (userInputIsStudentYesOrNot=="y") or \
   (userInputIsStudentYesOrNot =='yes') or (userInputIsStudentYesOrNot == 'YES'):
    booleanIsAdultOrStudent = True
else:
    booleanIsAdultOrStudent = False

print "the total cost for ", numberOfAdultTickets, " adult tickets and ", numberOfChildTickets, \
      " children tickets is = ",  \
      calculateCost (numberOfAdultTickets, numberOfChildTickets, booleanIsAdultOrStudent)


