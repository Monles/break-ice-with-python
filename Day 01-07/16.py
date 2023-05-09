# Question 16
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9
# Then, the output should be:

# 1,9,25,49,81
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

a = input().split(',')

seq = []
lst = [int(i) for i in a]

for j in lst:
  if j % 2 != 0:
    j = j * j
    seq.append(j)

seq = [str(i) for i in seq]
print(','.join(seq))

# Another method

# a = input().split(',')
# lst = [int(i) for i in a]


# def flt(x):
#   return x % 2 != 0


# seq = [str(i * i) for i in filter(flt, lst)]
# print(",".join(seq))
