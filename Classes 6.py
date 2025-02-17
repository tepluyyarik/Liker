class Animal:
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.poison = poison
        self.nuke = nuke
        self.blood = blood
    def info(self):
        print(f"Name   - {self.name}")
        print(f"Age - {self.age}")

class Reptiles(Animal):
    weight = 100
    nuke = 23
class Arthropoda(Animal):
    poison = 30
    blood = 45


animal = Animal("Someone", 5)
#print(animal.weight)
animal.info()
print()

reptiles = Reptiles("Snake, Salamandra", 12, weight=88, nuke=17)
#print(reptiles.nuke)
#print(reptiles.weight)
reptiles.info()

arthropod = Arthropoda("Spider,Bee", 21, poison=34, blood=42)
#print(arthropod.poison)
#print(arthropod.blood)
class Snake(Reptiles):
    length = 46

class Bee(Arthropoda):
    honey = 28

class Salamandra(Reptiles):
    stain = 57

class Spider(Arthropoda):
    eyes = 6

    def info(self):
        print(self.eyes)
def info(self):
    print(f"Name   - {self.name}")
    print(f"Age - {self.age}")
    print(f"Weight - {self.weight}")
    print(f"Poison - {self.poison}")
    print(f"Nuke - {self.nuke}")
    print(f"Blood - {self.blood}")

spider = Spider("Tarantula", 1, 69, 36, 15, 48)
spider.info()

snake = Snake("Anaconda", 2,56, 47, 26, 39 )
snake.info()

bee = Bee("Common", 0.3, 43, 32, 24, 35)
bee.info()

salamandra = Salamandra("Black", 3, 106, 21, 30, 40)
salamandra.info()


class Animal:
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.poison = poison
        self.nuke = nuke
        self.blood = blood

    def info(self):
        print(f"Name   - {self.name}")
        print(f"Age - {self.age}")
        print(f"Weight - {self.weight}")
        print(f"Poison - {self.poison}")
        print(f"Nuke - {self.nuke}")
        print(f"Blood - {self.blood}")


class Reptiles(Animal):
    def __init__(self, name, age=None, weight=100, poison=None, nuke=23, blood=None):
        super().__init__(name, age, weight, nuke)


class Arthropoda(Animal):
    def __init__(self, name, age=None, weight=None, poison=30, nuke=None, blood=45):
        super().__init__(name, age, poison, blood)


animal = Animal("Someone", 5)
animal.info()
print()

reptiles = Reptiles("Snake, Salamandra", 12, weight=88, nuke=17)
reptiles.info()
print()

arthropod = Arthropoda("Spider,Bee", 21, poison=34, blood=42)
arthropod.info()
print()


class Snake(Reptiles):
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None, length=46):
        super().__init__(name, age, weight, nuke)
        self.length = length

    def info(self):
        super().info()
        print(f"Length - {self.length}")


class Bee(Arthropoda):
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None, honey=28):
        super().__init__(name, age, poison, blood)
        self.honey = honey

    def info(self):
        super().info()
        print(f"Honey - {self.honey}")


class Salamandra(Reptiles):
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None, stain=57):
        super().__init__(name, age, weight, nuke)
        self.stain = stain

    def info(self):
        super().info()
        print(f"Stain - {self.stain}")


class Spider(Arthropoda):
    def __init__(self, name, age=None, weight=None, poison=None, nuke=None, blood=None, eyes=6):
        super().__init__(name, age,weight, poison)
        self.eyes = eyes

    def info(self):
        super().info()
        print(f"Eyes - {self.eyes}")


spider = Spider("Tarantula", 1, 69, 36, 15, 48)
spider.info()
print()

snake = Snake("Anaconda", 2, 56, 47, 26, 39)
snake.info()
print()

bee = Bee("Common", 0.3, 43, 32, 24, 35)
bee.info()
print()

salamandra = Salamandra("Black", 3, 106, 21, 30, 40)
salamandra.info()
print()
