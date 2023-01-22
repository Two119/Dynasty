from assets.scripts.core_funcs import *
class Hunter:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.color = (255, 0, 0)
        self.radius = 20
        self.dest = None
        self.speed = round(9/6)
    def update(self, ecosys):
        if not hasattr(self, "circ_surf"):
            self.circ_surf = pygame.Surface((50, 50))
            pygame.draw.circle(self.circ_surf, self.color, (25, 25), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)
        if self.dest == None:
            for being in ecosys.beings:
                if being.pos[0] in range(self.pos[0]-(self.radius*5), self.pos[0]+(self.radius*5)) and being.pos[1] in range(self.pos[1]-(self.radius*5), self.pos[1]+(self.radius*5)):
                            self.dest = being
        if self.dest == None:
            pass
        else:
            food_exist = False
            for being in ecosys.beings:
                if being == self.dest:
                    food_exist = True
                if hasattr(being, "mask"):
                    if being.mask.overlap(self.mask, (self.pos[0]-being.pos[0], self.pos[1]-being.pos[1])) == None:
                                pass
                    else:
                        being.en = -100
            if not food_exist:
                self.dest = None
                return
            if self.pos[0]-self.dest.pos[0] > 0:
                self.pos[0]-=(self.speed)
            else:
                self.pos[0]+=self.speed
            if self.pos[1]-self.dest.pos[1] > 0:
                self.pos[1]-=(self.speed)
            else:
                self.pos[1]+=self.speed
            if hasattr(self.dest, "mask"):
                if self.dest.mask.overlap(self.mask, (self.pos[0]-self.dest.pos[0], self.pos[1]-self.dest.pos[1])) == None:
                            pass
                else:
                    self.dest.en = -100
        win.blit(self.circ_surf, self.pos)
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)