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
            self.beings.append(Being([random.randint(0, win_size[0]), random.randint(0, win_size[1])], [random.randint(10, 15), 2, random.randint(75, 125), [0, 0, 255]]))
        for i in range(args[1]):
            self.enemies.append(Hunter([random.randint(round(win_size[0]*1/40), round(win_size[0]*3/4)), random.randint(round(win_size[1]*1/40), round(win_size[1]*3/4))]))
        if args[3]:
            self.beings[random.randint(0, len(self.beings)-1)].auto = False
        self.is_interactive = args[3]
        self.clock = pygame.time.Clock()
        self.dt = 1
    def update(self):
        self.clock.tick(120)
        if self.clock.get_fps() != 0:
            self.foodmanager.update(self)
            player = False
            for being in self.beings:
                    being.update(self)
                    if being.auto == False:
                        player = True
            for enemy in self.enemies:
                    enemy.update(self)
            avg = 0
            num = 0
            if len(self.beings) != 0:
                for being in self.beings:
                    num += 1
                    avg += being.radius
                avg /= num
            avg_2 = 0
            num = 0
            if len(self.beings) != 0:
                for being in self.beings:
                    num += 1
                    avg_2 += being.speed
                avg_2 /= num
            avg_3 = 0
            num = 0
            if len(self.beings) != 0:
                for being in self.beings:
                    num += 1
                    avg_3 += being.en
                avg_3 /= num
            if not self.is_interactive and not player:
                win.blit(ui_f.render("Avg Herbivore Energy"+": "+str(avg_3), False, (255, 202, 24)), [100, 50])
                win.blit(ui_f.render("Avg Herbivore Speed"+": "+str(avg_2), False, (255, 202, 24)), [100, 150])
                win.blit(ui_f.render("Avg Herbivore Radius (Size)"+": "+str(avg), False, (255, 202, 24)), [100, 250])
                win.blit(ui_f.render("Herbivores"+": "+str(len(self.beings)), False, (255, 202, 24)), [100, 350])
                win.blit(ui_f.render("Carnivores"+": "+str(len(self.enemies)), False, (255, 202, 24)), [100, 450])
        
            
            

                
        