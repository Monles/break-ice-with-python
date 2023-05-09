# Question 21
# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

from math import sqrt

pos = [0, 0]
lst = []

while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        pos[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        pos[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        pos[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        pos[1] += int(i.strip('RIGHT '))

print(round(sqrt(pos[0]**2 + pos[1]**2)))
