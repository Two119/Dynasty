from assets.scripts.core_funcs import *
class Being:
    def __init__(self, pos, genes=None) -> None:
        self.pos = pos
        self.genes = genes
        self.hungry = True
        self.dest = None
        self.cur_vel = None
        self.cur_vel_frames_count = False
        self.cur_vel_frames = 0
        self.parent = False
        self.cur_dir = None
        self.sighted_food = False
        self.speed = round(self.genes[gene_dict["speed"]]/6)
        self.en = 0.5
        self.radius = round(self.genes[gene_dict["size"]]/10)
        self.color = self.genes[gene_dict["color"]]
    def update(self, ecosys):
        self.en -= (0.0015/2)

        if self.en <= 0:
            ecosys.beings.remove(self)
            print("ded")
            del self
            return
        if self.dest == None:
            if self.cur_vel_frames_count:
                self.cur_vel_frames += 1
            if self.cur_vel == None and self.cur_dir == None:
                self.cur_vel = round(random.randint(0, 10)/10)
                self.cur_dir = round(random.randint(-10, 10)/10)
                self.cur_vel_frames_count = True
            if self.cur_vel_frames >= 90:
                self.cur_vel = round(random.randint(0, 10)/10)
                self.cur_dir = round(random.randint(-10, 10)/10)
                self.cur_vel_frames = 0
        else:
            food_exist = False
            for meal in ecosys.foodmanager.food:
                if meal[0] == self.dest:
                    food_exist = True
            if not food_exist:
                self.dest = None
                return
            if self.pos[0]-self.dest[0] > 0:
                self.pos[0]-=(self.speed)
            else:
                self.pos[0]+=self.speed
            if self.pos[1]-self.dest[1] > 0:
                self.pos[1]-=(self.speed)
            else:
                self.pos[1]+=self.speed
            if round(self.pos[0]-self.dest[0]) == 0 and round(self.pos[1]-self.dest[1]) == 0:
                self.dest = None
        if not hasattr(self, "circ_surf"):
            self.circ_surf = pygame.Surface((25, 25))
            pygame.draw.circle(self.circ_surf, self.color, (12.5, 12.5), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
        win.blit(self.circ_surf, self.pos)
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)
        if self.cur_vel != None and self.dest == None:
            self.pos[self.cur_vel]+=(self.speed*self.cur_dir)
