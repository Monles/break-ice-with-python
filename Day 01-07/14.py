# Question 14

# Question:

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:

# In case of input data being supplied to the question, it should be assumed to be a console input.

word = input()
upper, lower = 0, 0

for i in word:
  if i.isupper():
    upper += 1
  elif i.islower:
    lower += 1

print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")

# Another method
# word = input()

# upper = sum(1 for i in word if i.isupper())
# lower = sum(1 for i in word if i.islower())

# print(f"UPPER CASE {upper}")
# print(f"LOWER CASE {lower}")
