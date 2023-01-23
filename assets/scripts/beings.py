from assets.scripts.core_funcs import *
class Being:
    def __init__(self, pos, genes=None) -> None:
        self.pos = pos
        self.genes = genes
        self.hungry = True
        self.hunter = None
        self.dest = None
        self.cur_vel = None
        self.cur_vel_frames_count = False
        self.cur_vel_frames = 0
        self.hunted = False
        self.parent = False
        self.cur_dir = None
        self.sighted_food = False
        self.speed = round(self.genes[gene_dict["speed"]]/6)
        self.en = 0.5
        self.radius = round(self.genes[gene_dict["size"]]/10)
        self.color = self.genes[gene_dict["color"]]
    def update(self, ecosys):
        self.en -= (0.0015/5)
        self.rect = pygame.Rect(self.pos[0]-self.radius*3, self.pos[1]-self.radius*3, self.radius*8, self.radius*8)
        #pygame.draw.rect(win, (255, 0, 0), self.rect)
        if self.en <= 0:
            ecosys.beings = [b for b in ecosys.beings if b != self]
            #print("ded")
            del self
            return
        if not self.hunted:
            if self.dest == None:
                if self.cur_vel_frames_count:
                    self.cur_vel_frames += 1
                if self.cur_vel == None and self.cur_dir == None:
                    self.cur_vel = round(random.randint(0, 10)/10)
                    self.cur_dir = round(random.randint(-10, 10)/10)
                    self.cur_vel_frames_count = True
                if self.cur_vel_frames >= 60:
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
                    self.pos[0]-=((self.speed*1))
                else:
                    self.pos[0]+=(self.speed*1)
                if self.pos[1]-self.dest[1] > 0:
                    self.pos[1]-=((self.speed*1))
                else:
                    self.pos[1]+=(self.speed*1)

        else:
            
            if self.pos[0]-self.hunter.pos[0] > 0:
                self.pos[0]+=((self.speed*1))
            else:
                self.pos[0]-=(self.speed*1)
            if self.pos[1]-self.hunter.pos[1] > 0:
                self.pos[1]+=((self.speed*1))
            else:
                self.pos[1]-=(self.speed*1)
        self.circ_surf = pygame.Surface((self.radius*2, self.radius*2))
        pygame.draw.circle(self.circ_surf, self.color, (self.radius, self.radius), self.radius)
        self.circ_surf.set_colorkey((0, 0, 0))
        win.blit(self.circ_surf, self.pos)
        self.mask = pygame.mask.from_surface(self.circ_surf)
        if self.pos[0] in [nu for nu in range(0, 1280)] and self.pos[1] in [nu_ for nu_ in range(0, 720)]:
            if self.cur_vel != None and self.dest == None:
                self.pos[self.cur_vel]+=((self.speed*1)*self.cur_dir)
        else:
            if self.pos[0] < 0:
                self.pos[0] = 0+self.radius*2
            if self.pos[1] < 0:
                self.pos[1] = 0+self.radius*2
            if self.pos[0] > 1280:
                self.pos[0] = 1280-self.radius*2
            if self.pos[1] > 720:
                self.pos[1] = 720-self.radius*2