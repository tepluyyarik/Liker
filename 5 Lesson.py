import random
class Human:
    def __init__(self, name, house, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 1000
        self.gladness = 50


    def work(self):
        pass

    def eat(self):
        pass

    def chill(self):
        pass

    def cleaning(self):
        pass

    def info(self):
        pass

    def live(self):
        pass

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
            print("Подорож не можлива, не вистачає пального")
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
        pass


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
        print(f"Будинок: запас їжі - {self.food}, забрудненність - {self.pollution}")
class Shop:
    def __init__(self, type):
        self.type = type
        self.balance = 1000
        self.time = 20

    def shopping(self, purchases, moneyl):
        purchases = random.randint(200, 1000)
        moneyl = balance =- purchases
        if moneyl < 200:
            print("Ти так закупився що потрібно працювати!")
        else:
            self.purchases -= 801
            self.moneyl += 200
            print("Ви сьогодні можете повчитися програмувати!")
    def add_moneyleft(self, balance):
        if self.moneyl < 200:
            self.moneyl + balance <=1999
            self.moneyl += balance
            print(f"Y нас є {moneyl}!")
        else:
            self.moneyl += 1000
            print("Ми достатньо багаті.")









