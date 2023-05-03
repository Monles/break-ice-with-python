# Question 12
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
lst = []

for i in range(1000, 3001):
    x = str(i)
    for j in str(i):
        if ord(j) % 2 != 0:
            flag = 0
        if flag == 1:
            lst.append(str(i))

print(",".join(lst))
