#List all Divisors of a number using while loop

x = 10
i =  1

while i <10: #Check if i is less or equal to 10, if true, goto the next instruction 
    if x%i == 0: #Check if x can be evenly divided using i
        print ("Divisor",i)
    i = i+1 #Increase the value of i by 1. 
