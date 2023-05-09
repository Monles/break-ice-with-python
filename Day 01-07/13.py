# Question 13
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

lst = []

for i in range(1000, 3001):
    flag = 1
    for j in str(i):
        if ord(j) % 2 != 0:
            flag = 0
    if flag == 1:
        lst.append(str(i))
print(",".join(lst))
