import random


class Human:
    def __init__(self, name, house, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 1000
        self.gladness = 50

    def shoping(self):
        if self.car == None:
            print("Ідем в магазин пішки")
        else:
            self.car.drive(random.randint(10, 50))
        self.money -= random.randint(5, 15)
        self.house.food += random.randint(1, 5)


    def work(self):
        salary = random.randint(40, 50)
        self.money += salary
        print(f"Сьогодні працюємо. Заробили {salary}$")

    def buycar(self, car_price, model):
        if self.money >= car_price:
            self.money -= car_price
            self.car = Car(model)
            print(f"{self.name} купив авто!")
        else:
            print(f"Тобі не вистачає {car_price - self.money}$")

    def eat(self):
        self.gladness += 5
        food = random.randint(1,5)
        if self.house.food - food > 0:
            self.house.food -= food
            print("Ми трошки поїли")
        else:
            print("Поїсти не вдалося, холодильник пустий")


    def chill(self):
        print("Сьогодні ми відпочиваємо")
        self.money -= random.randint(5, 10)
        self.house.pollution += random.randint(1, 5)
        self.gladness += random.randint(5, 10)

    def cleaning(self):
        percent = random.randint(1, 5)
        if percent == 5:
            print("Сьогодні генеральне приберання")
            self.house.pollution = 0
        else:
            print("Сьогодні тільки повитирали пилюку")
            self.house.pollution = max(0, self.house.pollution - random.randint(1, 3))

    def info(self):
        print(f"Гроші - {self.money}$")
        print(f"Задоволення - {self.gladness}")
        print(self.house)
        if self.car != None:
            print(self.car)

    def live(self, day):
        print(f" ---- День №{day} ----")
        if self.money > 6000 and self.car is None:
            self.buycar(5000, "Toyota")
            self.money - 5000
        self.work()
        self.shoping()
        self.eat()
        self.chill()

        if day % 5 == 0:
            self.cleaning()

        self.info()
        print()



    def is_alive(self):
        if self.money < 0:
            return False
        return True

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100


    def drive(self, length):
        rashod = length * 0.1
        if self.fuel - rashod < 0:
            print("Подорож на авто не можлива, не вистачає пального, треба йти пішки")
        else:
            self.fuel -= rashod
            self.state -= length * 0.01
            print(f"Ми проїхали {length} км, витратили {rashod} л пального")

    def add_fuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
            print(f"Ми заправили {fuel} л пального")
        else:
            self.fuel = 60
            print("Бак повний!")

    def __str__(self):
        return f"Авто: {self.model}, пальне - {self.fuel}л, справність - {self.state}%"


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Робота: {self.name}, зарплатня - {self.salary}$"

class House:
    def __init__(self):
        self.pollution = 0
        self.food = 0

    def __str__(self):
        return f"Будинок: запас їжі - {self.food}, забрудненність - {self.pollution}"


human = Human("Vasya", job=Job("Програміст", 1000), house=House())
for day in range(1, 366):
    if human.is_alive() == False:
        break
    human.live(day)








