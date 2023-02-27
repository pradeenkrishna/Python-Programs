#Find the square root of a perfect square, with defensive programming.

x = 16 #bind x to a value
ans = 0  #A variable to save the answer; durng each loop the value changes until it reaches the answer

if x >= 0: #Before entering the while loop, check if x is greater than or equal to zero.

    while ans*ans < x: #While ans*ans is less than x, goto the next step
       ans =  ans +1 #add 1 to increase the value of ans and repeat the loop
    if ans*ans != x:  #After while loop ends it moves to the next instruction.
     print (x,"is not a perfect square")
    else:
        print (ans)

else:
    print (x,"is a negative number")
