# Question 34
# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

# 1
def square():
    lst = [i**2 for i in range(1, 21)]

    for i in range(5):
        print(lst[i])


square()

# 2
# def squares(n):
#   lst = [i**2 for i in range(1, n + 1)]
#   print(lst[0:5])


# squares(20)

# 3
func = lambda :print([i**2 for i in range(1,21)[:5]])