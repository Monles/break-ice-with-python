# Question 30
# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# Hints:
# Use len() function to get the length of a string.


def printStr(x, y):
    lenX = len(x)
    lenY = len(y)
    if lenX > lenY:
        print(x)
    elif lenY > lenX:
        print(y)
    else:
        print(x)
        print(y)


a, b = input().split()
printStr(a, b)
