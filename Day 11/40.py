# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.

text = input("Please type something. -->")
if text == "yes" or text == "Yes" or text == "YES" or text =="YEs" or text=="YeS" or text=="yeS":
    print("Yes")
else:
    print("No")