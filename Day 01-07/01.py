# 1)Find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).

# 2)The numbers obtained should be printed in a comma-separated sequence on a single line.

# My method
def a(x):
  
  if (x % 7 == 0 and x % 5 != 0):
    print(x, end=',')


print("\b")

for i in range(2000, 3200):
  a(i)

# for loop
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")