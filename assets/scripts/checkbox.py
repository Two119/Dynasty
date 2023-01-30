from assets.scripts.core_funcs import *
class CheckBox:
    def __init__(self, args):
        self.pos = args[0]
        self.checked = args[1]
        self.rect_surf = pygame.Surface((64, 64))
        self.mask = pygame.mask.from_surface(self.rect_surf)
        self.outlines = self.mask.outline()
        self.bg_surf = pygame.Surface((64, 64))
        self.bg_surf.set_colorkey((0, 0, 0))
        self.just_checked = False
    def update(self):
        self.bg_surf.fill((0, 0, 0))
        pygame.draw.lines(self.bg_surf, (45, 45, 45), True, self.outlines, 3)
        self.rect = pygame.Rect(self.bg_surf.get_width()/2-20, self.bg_surf.get_height()/2-20, 40, 40)
        if self.checked:
            pygame.draw.rect(self.bg_surf, (0, 255, 0), self.rect)
        if self.bg_surf.get_rect(topleft=self.pos).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if not self.just_checked:
                self.checked = not(self.checked)
                self.just_checked = True
        else:
            self.just_checked = False
        win.blit(self.bg_surf, self.pos)