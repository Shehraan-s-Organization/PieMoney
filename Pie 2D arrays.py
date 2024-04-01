#Input - Takes in the currency that the user is using, the cost of each type of pie, as well as the number of pies sold on each day

numbers = ["1","2","3","4","4","5","6","7","8","9","0"]
symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"," "]

#Symbolchecker - checks for symbols in an input
def symbol(word):
    for characters in word:
        if (characters in symbols)==True:
            return True
    return False

#Numberchecker - checks for numbers in an input
def number(word):
    for characters in word:
        if (characters in numbers)==True:
            return True
    return False

#Fruit adder - Adds the pies sold on each day
def cost(array):
    pies = 0
    for i in array:
        pies = pies + i
    return (pies)

total = [[],[],[],[]]
days = [" Monday: ", " Tuesday: ", " Wednesday: ", " Thursday: "]
day = days[0]
fruits = ["apple pies", "cherry pies", "blueberry pies"]
prices = []
redo = True

currency = input("Please enter the name of the currency that you are using: ")
while symbol(currency)==True or any(i.isalpha() for i in currency)==True or number(currency)==True:
    if symbol(currency)==True:
        print("Error, you entered a symbol which is an invalid input. Please only enter the name of your currency.")
        currency = input("Please enter the name of the currency that you are using: ")
    elif number(currency)==True:
        print("Error, you have entered a number. Please only enter the name of your currency.")
        currency = input("Please enter the name of the currency that you are using: ")
    elif any(i.isalpha() for i in currency)==True:
        break

while redo==True:
    for i in range(3):
        price = input("Please enter the cost of "+fruits[i]+": ")
        while symbol(price)==True or any(i.isalpha() for i in price)==True or number(price)==True:
            if symbol(price)==True:
                print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
                price = input("Please enter the cost of "+fruits[i]+": ")
            elif any(i.isalpha() for i in price)==True:
                print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
                price = input("Please enter the cost of "+fruits[i]+": ")
            elif number(price)==True:
                if float(price)<0:
                    print("Error, you have entered a negative price which is not possible. Please enter a positive number.")
                    price = input("Please enter the cost of "+fruits[i]+": ")
                elif float(price)==0:
                    print("Error, you have entered 0 which is not possible. Please enter the true cost.")
                    price = input("Please enter the cost of "+fruits[i]+": ")
                else:
                    prices.append(float(price))
                    break
    while True:             
        for i in range(3):
            sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
            while sold=="-" or symbol(sold)==True or any(i.isalpha() for i in sold)==True or number(sold)==True or sold % 1 != 0:
                if symbol(sold)==True:
                    print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
                    sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
                elif any(i.isalpha() for i in sold)==True:
                    print("Error, you entered a letter which is an invalid input. Please only enter a positive number.")
                    sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
                elif number(sold)==True:
                    if float(sold) % 1 != 0:
                        print("Error, you entered a decimal number which is an invalid input. Please only enter a whole number.")
                        sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
                    elif float(sold)<0:
                        print("Error, you have entered a negative number of pies which is not possible. Please enter a positive number.")
                        sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
                    else:
                        #Process - Multiplies the number of each pie sold, by its cost. Also then sorts these sales in a 2D array, based on the day that it was sold on. 
                        #Cost depending on which fruit
                        if i == 0:
                            fruitCost = int(sold)*float(prices[i])
                        elif i == 1:
                            fruitCost = int(sold)*float(prices[i])
                        elif i == 2:
                            fruitCost = int(sold)*float(prices[i])
                        #Add cost to day
                        if day == days[0]:
                            total[0].append(fruitCost)
                        elif day == days[1]:
                            total[1].append(fruitCost)
                        elif day == days[2]:
                            total[2].append(fruitCost)
                        else:
                            total[3].append(fruitCost)
                        break
                elif sold=="-":
                    print("Error, you entered a symbol which is an invalid input. Please only enter a positive number.")
                    sold = input("Please enter the number of "+fruits[i]+" sold on"+day)
        if day == days[0]:
            day = days[1]
        elif day == days[1]:
            day = days[2]
        elif day == days[2]:
            day = days[3]
            
    #Output - Diplays the profit from pie sales on each day
        else:
            print("\nPie sales on Monday: "+str(round(cost(total[0]),2))+" "+currency)
            print("\nPie sales on Tuesday: "+str(round(cost(total[1]),2))+" "+currency)
            print("\nPie sales on Wednesday: "+str(round(cost(total[2]),2))+" "+currency)
            print("\nPie sales on Thursday: "+str(round(cost(total[3]),2))+" "+currency)
            
            redo = (input("\nIf you would like to use this program again for another week, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
            while redo!="y" and redo!="n":
                print("Error, please enter one of the given options")
                redo = (input("If you would like to use this program again for another week, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
            if redo=="n":
                redo = False
                break
            else:
                day=days[0]
                print("\nRestarting program\n")
                redo = True
                break