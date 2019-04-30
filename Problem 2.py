#Deshawn Smith
#4/30/2019

#This program will give you a students name and major.


class student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = student("Deshawn", "Computer Science")
p2 = student("Melenie", "Applied Communications")


print(p1.name)
print(p1.major)

p1.myfunc()


p1.major = "Computer Science"

print(p1.major)

del p1.major

#print(p1.major)
print(p2.major)

del p1
