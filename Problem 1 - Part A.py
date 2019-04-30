#Deshawn Smith
#4/23/2019

#This program will give you a factorial answer.

def fac(number):
    if number == 0:
        return 1    
    else:
        answer = 1
        for x in range(1,number + 1):
            answer *= x

        print (answer)
fac(15)
