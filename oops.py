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

"""#python inheritance
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
"""
class product:
    def __init__(self, brand, type, function, vitamins, color, texture, scent):
        self.brand = brand
        self.type = type
        self.function = function
        self.vitamins = vitamins
        self.color = color
        self.texture = texture
        self.scent = scent
    def details(self):
        print(f"This product is under the brand of {self.brand} and is a {self.type}. Its function is to {self.function} and it has {self.vitamins}. It's {self.color} in color and is {self.texture}. It has {self.scent}.")

p1 = product("Simple", "facial wash", "wash away make-up, remove impurities and cleanse and refresh the skin", "vitamin C", "iridescent white", "slippery and soapy", "no scent")
p2 = product("Lush", "cuticle and hand butter", "nourish nails and rough skin", "beeswax, shea butter and avocado oil", "bright lemony yellow", "soft, creamy and slightly exfoliating", "a warm and vibrant lemon scent")
p3 = product("Lush", "hand cream", "provide intense hydration and nourishment", "shea, cashew and almond butter and rose water with chamomile blue oil, plus evening primrose oil", "almond white", "creamy and slightly exfoliating due to small black beads", "a subtle herbal scent")

p1.details()
print(p3.brand)
p2.texture = "balmy and slightly exfoliating"
p3.details()