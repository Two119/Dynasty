from assets.scripts.beings import *
from assets.scripts.hunter import *
from assets.scripts.foodmanager import *
class EcoSytem:
    def __init__(self):
        self.foodmanager = FoodManager()
        self.beings = []
        self.enemies = []
        for i in range(100):
            self.beings.append(Being([random.randint(0, 1280), random.randint(0, 720)], [random.randint(5, 10), 2, random.randint(75, 125), [0, 0, 255]]))
        for i in range(3):
            self.enemies.append(Hunter([random.randint(0, 1280), random.randint(0, 720)]))
    def update(self):
        self.foodmanager.update(self)
        for being in self.beings:
                being.update(self)
        for enemy in self.enemies:
                enemy.update(self)
        avg = 0
        num = 0
        for being in self.beings:
            num += 1
            avg += being.speed
        print(avg/num)
            
        