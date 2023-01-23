from assets.scripts.beings import *
from assets.scripts.hunter import *
from assets.scripts.foodmanager import *
class EcoSytem:
    def __init__(self):
        self.foodmanager = FoodManager()
        self.beings = []
        self.enemies = []
        for i in range(10):
            self.beings.append(Being([random.randint(0, 1280), random.randint(0, 720)], [random.randint(5, 10), 2, random.randint(75, 125), [0, 0, 255]]))
            if i in [4, 5]:
                self.enemies.append(Hunter([random.randint(320, 960), random.randint(180, 540)]))
        self.clock = pygame.time.Clock()
        self.dt = 1
    def update(self):
        self.clock.tick(120)
        if self.clock.get_fps() != 0:
            self.foodmanager.update(self)
            for being in self.beings:
                    being.update(self)
            for enemy in self.enemies:
                    enemy.update(self)
            avg = 0
            num = 0
            for being in self.beings:
                num += 1
                avg += being.radius
            avg /= num
            avg_2 = 0
            num = 0
            for being in self.beings:
                num += 1
                avg_2 += being.speed
            avg_2 /= num
            print([avg, avg_2])

                
        