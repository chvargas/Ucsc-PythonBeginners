#    You own a restaurant. In your restaurant, you sell the following:
#    Hamburger $3 each
#    Hot Dog     $2 each
#    Milk Shake   $3 each
#    Start by writing a function with a name like ‘calculateBill’ that will do the following:
#    - Allow the caller to pass in three parameters:
#     the number of hamburgers to buy
#     the number of hot dogs to buy
#     the number of milk shakes to buy 
#    - Calculate the subtotal of this purchase, by doing some simple math. 
#    - Add 10% of that amount for tax, to get a total
#    - it should return the total amount for the purchase
#    - The calculateBill function should NOT print anything, only the main code should do the printing.

#    Then write 3 calls to the function:
#    The first two calls should use different amounts of hamburgers, hot dogs, and milk shakes.  To verify that your function works correctly, test with these values: 
#    3 hamburgers, 2 hot dogs, and 1 milk shake. 
#    This order should come out to (16.00 plus 1.60 tax) 17.60.
#    8 hamburgers, 8 hot dogs, and 8 milkshakes 
#    This order should give a cost  70.40

#    Then write 3 calls to the function:
#    The first two calls should use different amounts of hamburgers, hot dogs, and milk shakes.  To verify that your function works correctly, test with these values: 
#    3 hamburgers, 2 hot dogs, and 1 milk shake.


    
def  calculateBill():
     print '-----------------------------------------------------------------------------------------------------'

     priceHamburguer = 3
     priceHotDog = 2
     priceMilkShake = 3

     numberOfHamburguersToBuy = raw_input('the number of hamburgers to buy')
     numberOfHamburguersToBuy = int(numberOfHamburguersToBuy)

     numberOfHotDogsToBuy = raw_input('the number of hot dogs to buy')
     numberOfHotDogsToBuy = int(numberOfHotDogsToBuy)

     numberOfMilkShakesToBuy = raw_input('the number of milk Shakes to buy')
     numberOfMilkShakesToBuy = int(numberOfMilkShakesToBuy)
          
     
     subTotalAmount = (numberOfHamburguersToBuy * priceHamburguer) + (numberOfHotDogsToBuy * priceHotDog) + (numberOfMilkShakesToBuy * priceMilkShake)
     print 'The subtotal is :', subTotalAmount
     totalTaxes = subTotalAmount * 0.10
     print 'The Total of Taxes is :',totalTaxes
     totalAmount = subTotalAmount + totalTaxes
     print 'The total amount is: ', totalAmount
     return calculateBill
     
calculateBill()

priceHamburguer = 3
priceHotDog = 2
priceMilkShake = 3
print 'The sum of the bill in the function number 1 is :' ,(((priceHamburguer  * 3) + (priceHotDog * 2) + (priceMilkShake * 1))*(1.10))

 #  8 hamburgers, 8 hot dogs, and 8 milkshakes
print 'The sum of the  bill in the function number 2 is :' ,(((priceHamburguer  * 8) + (priceHotDog * 8) + (priceMilkShake * 8))*(1.10))

print 'The total of function number 1 and function number 2 is :', ((((priceHamburguer  * 3) + (priceHotDog * 2) + (priceMilkShake * 1))*(1.10)) + (((priceHamburguer  * 8) + (priceHotDog * 8) + (priceMilkShake * 8))*(1.10)))
