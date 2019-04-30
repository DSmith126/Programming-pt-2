#Deshawn Smith
#04/16/2019

#Problem 6 this will ask the user for a number and give an error if the number is over 20.

x = int(input("Please enter a number. "))

if x > 20:
    raise Exception("Sorry that number is to big.")

else:
    print(x)
