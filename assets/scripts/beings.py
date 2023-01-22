from assets.scripts.core_funcs import *
class Being:
    def __init__(self, pos, genes=None, parents=None) -> None:
        self.pos = pos
        self.genes = genes
        self.hungry = True
        self.en = 0
        if parents == None:
            self.speed = self.genes[gene_dict["speed"]]
            self.energy_needed = self.genes[gene_dict["energy"]]
            self.radius = self.genes[gene_dict["size"]]/10
            self.color = self.genes[gene_dict["color"]]
        else:
            self.speed = random.randint(parents[0].genes[gene_dict["speed"]], parents[1].genes[gene_dict["speed"]])
            self.energy_needed = random.randint(parents[0].genes[gene_dict["energy"]], parents[1].genes[gene_dict["energy"]])
            self.radius = random.randint(parents[0].genes[gene_dict["size"]], parents[1].genes[gene_dict["size"]])
            col_num = random.randint(0, 1)
            self.color = parents[col_num].genes[gene_dict["color"]]
    def update(self, ecosys):
        if self.en >= 2:
            self.hungry = False
        if not self.hungry:
            ecosys.beings.append(Being([random.randint(0, 1280), random.randint(0, 720)], [random.randint(5, 10), 2, random.randint(75, 125), [0, 0, 255]]))
        
        if not hasattr(self, "circ_surf"):
            self.circ_surf = pygame.Surface((25, 25))
            pygame.draw.circle(self.circ_surf, self.color, (12.5, 12.5), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
        win.blit(self.circ_surf, self.pos)
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)