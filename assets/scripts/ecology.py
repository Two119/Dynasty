from assets.scripts.beings import *
from assets.scripts.button import *
from assets.scripts.hunter import *
from assets.scripts.foodmanager import *
class EcoSytem:
    def __init__(self, args):
        self.foodmanager = FoodManager(args[2])
        self.beings = []
        self.enemies = []
        self.gen_num = 0
        self.font = pygame.font.SysFont("Calibri", 20, True, False)
        self.death_text = pygame.font.Font("PrinceValiant.ttf", 90).render("Your lineage has ended!", False, (255, 202, 24))
        for i in range(args[0]):
            self.beings.append(Being([random.randint(0, win_size[0]), random.randint(0, win_size[1])], [random.randint(5, 10), 2, random.randint(75, 125), [0, 0, 255]]))
        for i in range(args[1]):
            self.enemies.append(Hunter([random.randint(round(win_size[0]*1/40), round(win_size[0]*3/4)), random.randint(round(win_size[1]*1/40), round(win_size[1]*3/4))]))
        self.beings[random.randint(0, len(self.beings)-1)].auto = False
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
            
        
            
            

                
        