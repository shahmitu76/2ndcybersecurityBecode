#*. Use variables to represent the price of materials.**  
#- 2 bottles of milk at €0.45 each
#- 3 bottles of raw cider at €3.85 each
#- 1 bag of flour at 0.9 €
#- 1 packet of butter at €0.77
#- 1 jar of nutella at €1.87  

#**Calculate the sum of all items and store it in a `orderPrice` variable**

bottleofmilk=0.45/2
bottleofrawcider=3.85/3
bagofflour=0.9
packetOfButter=0.77
jarOfNuttela=1.87
orderPrice=2*bottleofmilk+3*bottleofrawcider+bagofflour+packetOfButter+jarOfNuttela
print("orderprice={}".format(orderPrice))
#Create a variable `allowanceMoney` which has a value of 20 and then create an algorithm that calculates the available money by subtracting the price of the order.**

#If there is enough money, record the following sentence in the variable `message` and subtract the expense from `allowanceMoney` : 
# message = "You have spent" + `orderPrice` + "you have left" + `allowanceMoney` 

#If there is not enough money, record the following sentence in the `message` variable: 
#- message= "Sorry you're missing *amountMissing* euros" 

#If there is 0 left, record the following sentence in the `message` variable: 
#- message = "You are broke!" #
allowanceMoney=20
allowanceMoney=allowanceMoney-orderPrice
print("allowance money is {}".format(allowanceMoney))
if allowanceMoney!=0 and allowanceMoney>=orderPrice:
    print("You have spent{} and you are left with {}".format(orderPrice,allowanceMoney))
elif allowanceMoney<orderPrice:
    print("Sorry, you are missing {} euros".format(orderPrice))
elif allowanceMoney==0:
    print("you are broke")
    