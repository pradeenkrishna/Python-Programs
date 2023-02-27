##Farmyard problem using brute force method or enumerate & Check

def solve (numberoflegs, numberofheads): ##function solve
    
    for numberofchicken in range (0, numberofheads + 1): 
        numberofpigs = numberofheads - numberofchicken 
        totallegs = 4 * numberofpigs + 2 * numberofchicken
        if totallegs == numberoflegs:
            return [numberofpigs, numberofchicken]
    return [None, None] ##If no answer is found, return none as tuple to the interpreter


def barnyard():  ##Creating another function to call previous function.
    
    heads = int(input("Enter the number of heads: "))
    legs = int(input("Enter the number of legs: "))
    pigs, chickens = solve(legs, heads)
    if pigs == None: ##Check if the function solve returned any value or not. 
        print ("There is no solution")
    else:
        print ("Number of pigs: ", pigs)
        print ("Number of chickens: ", chickens)

def solve1(numberoflegs, numberofheads):

    for numberofspiders in range (0, numberofheads+1):
        for numberofchickens in range (0, numberofheads - numberofspiders +1):
            numberofpigs = numberofheads - numberofchickens - numberofspiders
            totallegs = 4 * numberofpigs + 2 * numberofchickens + 8 * numberofspiders
            if totallegs == numberoflegs:
                return [numberofpigs, numberofchickens, numberofspiders]
    return [None, None, None]

def barnyard1():  ##Creating another function to call previous function.
    
    heads = int(input("Enter the number of heads: "))
    legs = int(input("Enter the number of legs: "))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None: ##Check if the function solve returned any value or not. 
        print ("There is no solution")
    else:
        print ("Number of pigs: ", pigs)
        print ("Number of chickens: ", chickens)
        print ("Number of spiders: ", spiders)

def solve2(numberoflegs, numberofheads):

    for numberofspiders in range (0, numberofheads+1):
        solutionfound = False
        for numberofchickens in range (0, numberofheads - numberofspiders +1):
            numberofpigs = numberofheads - numberofchickens - numberofspiders
            totallegs = 4 * numberofpigs + 2 * numberofchickens + 8 * numberofspiders
            if totallegs == numberoflegs:
                print ("Number of pigs: " + str(numberofpigs) + ',')
                print ("Number of Chickens: " + str(numberofspiders) + ',')
                print ("Number of spiders: ", numberofspiders)
                solutionfound = True 
    if not solutionfound:
            print ("There is no solution")











