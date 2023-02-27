#This is a simple program which suquares an integer by doing iterations. 

x = 3 #binding x to value 3
ans = 0 #Initial value of Y is set to 0, but it will change and increase with each loop.
iteration_left = x #A variable to keep a count on how many loops to complete. 

while (iteration_left > 0): # A while loop that checks to see whether the variable "iteration left" is larger than zero and executes the next block of code if it is true.
    ans = ans + x   #adding value of x to y and binding the result to Y itself. 
    iteration_left = iteration_left - 1 #During each loop; decrease the value of the variable "iteration left" by 1.
    
print (ans) #printing the total value of 'y' when the loop ends.


#The loop runs until it stops, at which point the value of Y increases, giving us the answer 9.
