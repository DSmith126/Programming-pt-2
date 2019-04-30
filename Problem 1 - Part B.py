#Deshawn Smith
#04/23/2019

#This function will be recursive and compute the factorial of a given number.

def fac(number):
    if number <1:
        return 1
    else:
        return number * fac(number - 1)

print(fac(n))
