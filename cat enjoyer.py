import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.kind = 8
        self.enjoyed = 44
        self.alive = True

    def sleep(self):
        self.kind += 1
        self.enjoyed -= 1
        print("Mrrмяумяумяу")


    def murtoowner(self):
        self.enjoyed += 1
        self.kind -= 1
        print("Mereeuimer :)")


    def dinamic(self):
        self.enjoyed -= 0.5
        self.kind -=0.22
        print("Мяу мя ...")



    def toiletmatter(self):
        self.kind += 0.33
        print("pffffff")

    def is_alive(self):
        if self.enjoyed < 0:
            print("Мярмунххххх ...")
            self.alive = False
        elif self.kind < 0:
            print("мммммммммм")
            self.alive = False
        elif self.kind > 50:
            print("Мррррряууууууууу")
            self.alive = False

    def info(self):
        print(f"Вподобання - {self.enjoyed}")
        print(f"Стрес    - {self.kind}")


    def live(self, day):
        print()
        print(f"  ----- День №{day+1} -----")
        print(f"Mirrik {self.name}. ІMrunn:")
        rnd = random.randint(1,4)
        if rnd == 1:
            self.sleep()
        elif rnd == 2:
            self.murtoowner()
        elif rnd == 3:
            self.dinamic()
        elif rnd == 4:
            self.toiletmatter()
        self.info()
        self.is_alive()


cat = Cat("Vrungel")
for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)