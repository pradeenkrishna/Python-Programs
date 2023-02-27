#smallest of the three numbers

x= 5  #binding values to x,y and z. 
y= 4
z= 2
print (x,y,z)
if x < y and x < z:  #Condition test: If x is less than y and less than z then print 'x' as the least.
                     #If both 'and' conditions are false, move to next step and X is no longer less than both y and z. 
    print (x,'is the least')
elif y < z:
    print (y,'is the least') #y and z is only remaining, becuase x already failed the test so compare Y with z.
else:
    print (z,'is the least')

