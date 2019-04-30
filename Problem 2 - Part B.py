#Deshawn Smith
#04/23/2019

#This reverse the numbers/words in a list.

WordList = [32,54,66,29,18]
def reverse(words):
    return [words[-1]] + reverse(words[:-1]) if words else []

print(reverse(WordList))
