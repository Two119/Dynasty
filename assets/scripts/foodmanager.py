from assets.scripts.core_funcs import *
from assets.scripts.beings import *
class FoodManager:
    def __init__(self) -> None:
        self.food = []
        while len(self.food) < 25:
            num = random.randint(1, 10)
            if num == 3:
                self.food.append([[random.randint(0, 1280), random.randint(0, 720)], random.randint(5, 10)])
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
                            self.food.append([[random.randint(0, 1280), random.randint(0, 720)], random.randint(5, 10)])
                        being.en+=1
                if round(being.en) >= 3 and not being.parent:
                    if (being.speed*6) <= 10 and being.radius*10 <= 125:
                        ecosys.beings.append(Being([random.randint(0, 1280), random.randint(0, 720)], [random.randint((being.speed*6), (being.speed*18)), 2, random.randint((being.radius*5), (being.radius*20)), [0, 0, 255]]))
                        being.en = 0.5
                if meal[0][0] in range(being.pos[0]-(being.radius*5), being.pos[0]+(being.radius*5)) and meal[0][1] in range(being.pos[1]-(being.radius*5), being.pos[1]+(being.radius*5)):
                    being.sighted = True
                    being.dest = meal[0]
            if ecosys.enemies != []:
                for enemy in ecosys.enemies:
                    if hasattr(being, "mask"):
                        if meal[2].overlap(enemy.mask, (enemy.pos[0]-meal[0][0], enemy.pos[1]-meal[0][1])) == None:
                            pass
                        else:
                            if meal in self.food:
                                self.food = [m for m in self.food if m != meal]
                                self.food.append([[random.randint(0, 1280), random.randint(0, 720)], random.randint(5, 10)])
                            being.en+=1

                            