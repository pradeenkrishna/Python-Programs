##x = 10
##
##for i in range (1,x):
##    if x%i ==0:
##     print("Divisor = ", i)

x = 100
divisors = ()   #Using a tuple to store all the divisors  
for i in range (1,x):
    if x%i ==0:
        divisors  = divisors+(i,)

