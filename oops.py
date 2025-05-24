"""#creating a fruit class
class fruit:
    #creating the constructor
    def __init__(self, name, color, shape, texture, taste, country_og, nutrition):
        self.color = color
        self.shape = shape
        self.texture = texture
        self.taste = taste
        self.og = country_og
        self.nutri = nutrition
        self.name = name
    def details(self):
        print(f"This is a(n) {self.name} and it is {self.color}. It has a {self.shape} shape and tastes {self.taste}.")
        print(f"It is {self.texture} in texture.")
        print(f"It's from {self.og} and is high in {self.nutri}.")

f1 = fruit("apple", "red usually", "round", "often crunchy", "yummmy", "Kazakhstan", "fiber")
f2 = fruit("banana", "yellow", "curvy", "soft and fluffy", "sweet", "Papua New Guinea", "carbohydrates")
f3 = fruit("mango", "yellow/orange on the inside", "round", "slippery,creamy and soft", "delicious, tangy and sweet", "Myanmar", "vitamin B and C")

f1.details()
print(f3.og)
f3.texture = "creamy and soft"
f3.details()
"""

#python inheritance
class person:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
    def show(self):
        print(f"This person is called {self.name}. Their ID number is {self.id_num}.")

#child class
class employ(person):
    def __init__(self, name, id_num, salary, position):
        person.__init__(self, name, id_num)
        self.salary = salary
        self.position = position
    def details(self):
        print(f"This is {self.name} with the ID number of {self.id_num}. They have a salary of {self.salary} and are {self.position}.")

any = employ("Kiera", "9367", "£70,000", "CEO")
any.details()
any.show()