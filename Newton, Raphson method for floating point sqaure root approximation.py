##Newton, Raphson method

def squarerootNR(x, epsilon):


    assert x >= 0
    assert epsilon > 0, 'epsilon must be positive'

    x = float (x)
    guess = x/2.0
    diff = guess**2 -x  
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:

        ##print ("While loop ran")

        guess = guess -diff/(2.0*guess)
        diff = guess**2 -x
        ctr = ctr +1

    assert ctr <= 100, 'Iteration count exceeded'
    
    print ("Iterations: ", ctr ,"Guesses: ",guess)
    return guess
