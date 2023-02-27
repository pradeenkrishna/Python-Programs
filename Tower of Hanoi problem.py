## Recursive Python function to solve the tower of hanoi
 
def tower(n, A, B, C): #A = Source, B = Destination, C = Auxilliary
    if n>0:

        tower(n-1, A, C, B)
        print ("Move a disc from", A, "to", C)
        tower (n-1, B, A, C)
