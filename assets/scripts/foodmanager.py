from assets.scripts.core_funcs import *
class FoodManager:
    def __init__(self) -> None:
        self.food = []
        while len(self.food) < 20:
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
                        print('food')