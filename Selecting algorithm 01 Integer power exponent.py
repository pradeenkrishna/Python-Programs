##Finding the order of growth to find the best algorithm

def exp1(a,b): ##a = base value , b = exponent
     ans = 1
     while (b>0):
         ans = ans * a
         b = b-1
     return ans
    
def exp2 (a,b):
    if b == 1:
        return a
    else:
        return a*exp2(a, b-1) ##Using recursion

def exp3 (a,b):
    if b == 1:
        return a
    if (b//2) *2 == b:
         return exp3(a*a, b/2)
    else:
         return a*exp3 (a, b-1)

def g(n,m):
     x =0
     for i in range (n):
          print ("Entered first loop")
          for j in range(m):
               print ("Entered second loop")
               x += 1
     return x

