##examples of structured code

import math

#Get base
inputOk =  False 
while not inputOk:
    base = float(input('Enter base: '))
    if type(base) == type(1.0):
        inputOk = True
    else:
        print ("This is not a floating point number")

        
#Get height
inputOk =  False
while not inputOk:
    height = float(input ('Enter height: '))
    if type(height) == type(1.0):
        inputOk = True
    else:
        print ("Enter digit is not a floating point number")

hyp = math.sqrt(base*base + height*height)

#print ("Base" + str(base) + "Height" + str(height) + "hyp" + str(hyp))

print (hyp)

