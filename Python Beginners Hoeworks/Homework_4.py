# Build a program that simulates rounds of randomly rolling 2
# six-sided dice.  The program must keep track of the number of rounds,
# and check for and report when you roll a doubles. 

 
import random

def rollSingleDice():
    return random.randrange(1,7)

looping = True#Starting condition
numberOfRoundPlayed = 0
numberOfDoubles = 0

while looping == True:
    answer = raw_input ('\nPlease type YES to continue rolling the dices or Enter to exit : ')
    if answer == '':
        looping = False
    else:
        diceNumber1 = rollSingleDice()
        diceNumber2 = rollSingleDice()
        numberOfRoundPlayed = numberOfRoundPlayed +1 #increment the played round
        print 'Round played number ', numberOfRoundPlayed ,' the first dice was ' , diceNumber1 , 'the second dice was ', diceNumber2
        if diceNumber1 == diceNumber2:
            numberOfDoubles = numberOfDoubles + 1.0        
            print 'DOUBLES!', 'this is your double number : ', numberOfDoubles
            percentageOfDoubles = round(((numberOfDoubles / numberOfRoundPlayed) * 100),2)
            print 'The percentage of total doubles is ' , percentageOfDoubles ,"%", numberOfDoubles , 'out', numberOfRoundPlayed  
            
        
