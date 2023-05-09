# 1) With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).

# 2) and then the program should print the dictionary.

# 3) Suppose the following input is supplied to the program: 8

# 4) Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def a(n):
  b = {}
  for i in range(1, n+1):
    b[i] = i * i
  return b


c = int(input("Type a num: "))
print(a(c))
