'''Create a program that does some simple math on a list of numbers.
 Details:
- Build a loop.  Each time through the loop, ask the user to enter a number.
Your program should collect the numbers into a list - using
<yourListName>.append(<value>).
- The user can enter integers or floating point numbers, and your code
should convert whatever the user types into a floating point number.
- Allow the user to continue to input numbers until the user presses the
Return or the Enter key (at which point the resulting input will be the
empty string, ‘’).

Once the user has finished entering numbers, using one or more “for”
loop(s), your program should:

1) Print the resulting list
2) Determine and print out smallest number in the list
3) Determine and print the largest number in the list
4) Calculate and print the sum of all the numbers in the list
5) Calculate and print the average of all the numbers in the list

NOTE:  If you do some research, you will find that there are some
built-in list functions that will do these functions for you
(sum, min, max, sort, etc.).  Do NOT use these functions.
I want you to get the experience of writing “for” loops to iterate
through lists.

You do not need to build any functions to complete this assignment.
(Even if you don’t complete the full assignment, submit what you have –
I will give partial credit.)'''

looping = True #Starting condition
numbersList = [ ]
numbersListIntegers = [ ]
numbersListFloats = [ ]


numbersListNumeric = [int(i) for i in numbersList]


while looping == True:
    numberEntered = raw_input ('\nPlease enter a number or pres ENTER to exit : ')
        
    if numberEntered == '':
        looping = False
        
        print numbersList
            
    else:
        print 
        numbersList.append(numberEntered)
        #elif type(numberEntered) == float :
            #numbersListNumeric = [float(i) for i in numbersList]
         #   numbersList.append(numberEntered)
