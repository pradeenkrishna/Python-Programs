##Bisection method
def squarerootBi (x, epsilon):


    assert x >= 0
    assert epsilon > 0, 'epsilon must be positive'

    low = 0
    high = max(x, 1.0)

   

    guess = (low + high) / 2.0 ##Choose something in the middle
    ctr = 1
    
    print ("High = ", high)

    print("Guess = ", guess)

    while abs(guess**2 -x) > epsilon and ctr <= 100:

        print ("While loop ran")

        if guess**2 < x:
            low = guess

        else:
            high = guess

        guess = (low + high) /2.0
        ctr = ctr +1

    assert ctr <= 100, 'Iteration count exceeded'
    
    print ("Iterations: ", ctr ,"Guesses: ",guess)
    return guess
