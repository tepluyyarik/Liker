class Pet:
    count_of_pets = 3
    def __init__(self,name, long=235, heft = 160):
        self.long = long
        self.heft = heft
        self.name = name
        Pet.count_of_pets += 1
        print("Myay RRR")

    def grow_up(self, grow=16):
        if self.long + grow < 320:
            self.long += grow
        if self.heft + grow < 500:
            self.long += grow
    def info(self):
        print(f"Name   : {self.name}")
        print(f"Heft : {self.heft}")
        print(f"Long : {self.long}")

    def __str__(self):
        return f"Name   : {self.name}\nLong : {self.long}\nHeft : {self.heft}"

    def __del__(self):

        Pet.count_of_pets -= 3
        print(f"{self.name} is dead :(")

    def __len__(self):
        return self.heft

print(Pet.count_of_pets)

pet1 = Pet("Tiger")

pet1.grow_up(30)


print(pet1)

print(Pet.count_of_pets)
pet3 = Pet("Lion")

pet1.grow_up(27)


print(pet3)

print(Pet.count_of_pets)

pet2 = Pet("Croco", 400)
pet2.grow_up(40)
print(pet2)
print(Pet.count_of_pets)

print(len(pet2))