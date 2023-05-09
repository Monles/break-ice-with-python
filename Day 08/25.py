# Question 25
# Question:
# Define a class, which have a class parameter and have a same instance parameter.

# Hints:
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

class car:
    name = "Car"

    def __init__(self, name="none"):
        self.name = name


tesla = car("Tesla")
print("%s name is %s" % (car.name, tesla.name))

porsche = car()
porsche.name = "porsche"
print("%s name is %s" % (car.name, porsche.name))
