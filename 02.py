# 1) Write a program which can compute the factorial of a given numbers.

# 2) The results should be printed in a comma-separated sequence on a single line.

# 3) Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def fac(x):
  a = 1
  for i in range(1, x+1):
    a *= i
    print(f"{i} : {a}")


num = int(input("Type a num to compute the factorial: "))
fac(num)
