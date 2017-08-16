# -*- coding: cp1252 -*-
print' ___________________________________________________________________________________________________'
print 'Python Asignment 1 Christian Vargas'

#Creating Integers Variables
numOfWeeksYear = int (52)
numPythonStudents = int (35)
numParkingSpots = int (100)
numPlayersSoccerTeam = int (11) 
numTotalStudentsUcscExtension = int (250)

#Creating Float Variables
percentageTaxCalifornia = float (0.0875)
priceOfLaptopAsus = float (499.99)
gradeOfPythonStudent1 = float (4.55)
heightInMetersStudent1= float (1.82)

#Creating String Data Variables
nameStudent1= 'Christian Vargas'
monthsOfWinter= 'December, January and February'
namePilotFerrariNumber123= 'Michael Schumacher'
nameChampionSoccerWorldCup2014 = 'Germany'

# Creating Bolean Data Variables
isTheStudentTakingPython = True
isWinter = False
isCaliforniaASalesTaxesState = True
isThePilotFerrariNumber123Alive = False

print '\n 2)  Create a Python file (name ends in .py , e.g. IrvKalb_Homework1.py) that shows examples of '
print 'assignment statements using a total of 16 variables (4 integers, 4 floats , 4 strings, 4 booleans)'

print '___________________________________________________________________________________________________'
print 'The 4 integers variables are:'
print 'The number of weeks in a Year is : numOfWeeksYear =', numOfWeeksYear
print 'The number of Python students in UCSC Silicon Valley Extension is : numPythonStudents =', numPythonStudents
print 'The number of Parking spots in the campus is : numParkingSpots = ', numParkingSpots
print ' the number of players in a soccer team is : numPlayersSoccerTeam =', numPlayersSoccerTeam
print '\n'
print 'The 4 floats variables are:'
print 'The percentage of taxes in California is : percentageTaxCalifornia=' , percentageTaxCalifornia
print 'The price of a Assus Laptop is : priceOfLaptopAsus =', priceOfLaptopAsus
print 'The passing grade for the student number 1 was : gradeOfPythonStudent1 =' , gradeOfPythonStudent1
print 'The weight in Meters for the student number 1 is : heightInMetersStudent1 =' , heightInMetersStudent1
print '\n'
print 'The 4 strings variables are:'
print 'The name of the Student number 1 is: nameStudent1=', nameStudent1
print 'The months on winter time are: monthsOfWinter = ', monthsOfWinter
print 'The name of the pilot who drive the Ferrari number 123 is: namePilotFerrariNumber123=', namePilotFerrariNumber123
print 'Then name of the team who won the Soccer World Cup in 2014 was: nameChampionSoccerWorldCup2014 =', nameChampionSoccerWorldCup2014
print '\n'
print 'The 4 Bolean variables are:'
print 'The student is taking Python Clases in UCSC: isTheStudentTakingPython = ' , isTheStudentTakingPython
print 'Is winter Time: isWinter =' , isWinter
print 'Does California have Sales Taxes: isCaliforniaASalesTaxesState= ' , isCaliforniaASalesTaxesState
print 'Is the Pilot of the Ferrari number 123 Alive? : isThePilotFerrariNumber123Alive = ', isThePilotFerrariNumber123Alive 


#Doing Maths with the variables
print '___________________________________________________________________________________________________'
print '3 Math Operations with the variables'
print '\n'

finalPriceWithTaxes = priceOfLaptopAsus * ( 1+percentageTaxCalifornia )
print 'finalPriceWithTaxes = priceOfLaptopAsus * ( 1+percentageTaxCalifornia )'
print 'The final price for an Asus Laptop', priceOfLaptopAsus ,' including Taxes of 8.75% is =', finalPriceWithTaxes, '\n'

numSoccerMatchesInAYear = int (35)
relationNumSoccerMatchesVsNumWeeksPerYear = float (numOfWeeksYear) /  float (numSoccerMatchesInAYear)
print 'The relation between num of soccer matches', numSoccerMatchesInAYear, 'in a 52 weeks year  is =', relationNumSoccerMatchesVsNumWeeksPerYear, '\n'

relationNumParkingSpotsVsTotalStudensUcsc = numParkingSpots / numTotalStudentsUcscExtension
print 'The relation of Num of parking spots in UCSC vs Total of Students is =', relationNumParkingSpotsVsTotalStudensUcsc

