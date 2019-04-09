#Deshawn Smith
#04/09/2019

#Problem 2 this will tell you the number of day of the week you returned on.

day = int(input("number 0 - 6"))

gone = int(input("How long were you gone?"))

gone % 7

((gone % 7) + day) 
print(((gone % 7) + day) % 7)
