#Deshawn Smith
#4/9/2019

#Problem 6 this will give us 100 random numbers between 1 and 1000 then it will append the list

import random

n = []

for x in range(100):
    n.append(random.randrange(1,1000))

print (n)
