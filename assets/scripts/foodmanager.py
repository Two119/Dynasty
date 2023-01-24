from assets.scripts.core_funcs import *
from assets.scripts.beings import *
class FoodManager:
    def __init__(self, num_food) -> None:
        self.food = []
        while len(self.food) < num_food:
            num = random.randint(1, 10)
            if num == 3:
                self.food.append([[random.randint(0, win_size[0]), random.randint(0, win_size[1])], random.randint(5, 10)])
        self.circ_surf = pygame.Surface((32, 32))
        self.circ_surf.set_colorkey((0, 0, 0))
    def update(self, ecosys):
        for meal in self.food:
            pygame.draw.circle(self.circ_surf, (0, 255, 0), (16, 16), meal[1])
            if len(meal) == 2:
                meal.append(pygame.mask.from_surface(self.circ_surf))
            win.blit(self.circ_surf, meal[0])
            for being in ecosys.beings:
                if hasattr(being, "mask"):
                    if meal[2].overlap(being.mask, (being.pos[0]-meal[0][0], being.pos[1]-meal[0][1])) == None:
                        pass
                    else:
                        if meal in self.food:
                            self.food = [m for m in self.food if m != meal]
                            self.food.append([[random.randint(0, win_size[0]), random.randint(0, win_size[1])], random.randint(5, 10)])
                        being.en+=1
                if round(being.en) >= 3:
                    if being.auto:
                        ecosys.beings.append(Being([being.pos[0]+being.radius*2, being.pos[1]+being.radius*2], [random.randint((being.speed*3), (being.speed*9)), 2, random.randint((being.radius*5), (being.radius*15)), [0, 0, 255]]))
                        being.en = 0.5
                    else:
                        if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                            new = Being([being.pos[0]+being.radius*2, being.pos[1]+being.radius*2], [random.randint((being.speed*3), (being.speed*9)), 2, random.randint((being.radius*5), (being.radius*15)), [0, 0, 255]])
                            new.auto = False
                            ecosys.beings.append(new)
                            being.en = 0.5
                            being.auto = True
                if hasattr(being, "rect"):
                    if self.circ_surf.get_rect(topleft=meal[0]).colliderect(being.rect):
                        being.sighted = True
                        being.dest = meal[0]


                            