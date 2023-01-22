from assets.scripts.core_funcs import *
class Hunter:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.color = (255, 0, 0)
        self.radius = 20
    def update(self, ecosys):
        if not hasattr(self, "circ_surf"):
            self.circ_surf = pygame.Surface((50, 50))
            pygame.draw.circle(self.circ_surf, self.color, (25, 25), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
        win.blit(self.circ_surf, self.pos)
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)