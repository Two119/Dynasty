from assets.scripts.beings import *
from assets.scripts.hunter import *
from assets.scripts.foodmanager import *
class EcoSytem:
    def __init__(self):
        self.foodmanager = FoodManager()
        self.beings = []
        self.enemies = []
        for i in range(25):
            self.beings.append(Being([random.randint(0, 1280), random.randint(0, 720)], [random.randint(5, 10), 2, random.randint(75, 125), [0, 0, 255]]))
        for i in range(5):
            self.enemies.append(Hunter([random.randint(0, 1280), random.randint(0, 720)]))
        self.queue = [self.beings, self.enemies]
    def update(self):
        self.foodmanager.update(self)
        for group in self.queue:
            for creature in group:
                creature.update(self)
        