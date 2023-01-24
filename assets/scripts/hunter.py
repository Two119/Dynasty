from assets.scripts.core_funcs import *
class Hunter:
    def __init__(self, pos, genes=None) -> None:
        self.pos = pos
        self.color = (255, 0, 0)
        self.cur_dir = None
        self.en = 0.5
        self.dest = None
        self.cur_vel = None
        self.cur_vel_frames_count = False
        self.cur_vel_frames = 0
        if genes == None:
            self.radius = 15
            self.speed = round(18/6)
        else:
            self.radius = round(genes[gene_dict["size"]]/10)
            self.speed = round(genes[gene_dict["speed"]]/6)
    def update(self, ecosys):
        self.en -= (0.0015/5)
        self.rect = pygame.Rect(self.pos[0]-self.radius*4.5, self.pos[1]-self.radius*4.5, self.radius*12, self.radius*12)
        #pygame.draw.rect(win, (0, 255, 0), self.rect)
        if self.en <= 0:
            ecosys.enemies = [e for e in ecosys.enemies if e != self]
            #print("ded")
            del self
            return
        if round(self.en) >= 5:
            ecosys.enemies.append(Hunter([self.pos[0]+self.radius*2, self.pos[1]+self.radius*2], [random.randint(((self.speed*1)*3), ((self.speed*1)*9)), 2, random.randint((self.radius*5), (self.radius*15))]))
            self.en = 0.5
        if not hasattr(self, "circ_surf"):
            self.circ_surf = pygame.Surface((self.radius*2, self.radius*2))
            pygame.draw.circle(self.circ_surf, self.color, (self.radius, self.radius), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)
        if self.dest == None:
            for being in ecosys.beings:
                if being.circ_surf.get_rect(topleft=being.pos).colliderect(self.rect):
                    self.dest = being
                    being.hunted = True
                    being.hunter = self
        if self.dest == None:
            if self.cur_vel_frames_count:
                self.cur_vel_frames += 1
            if self.cur_vel == None and self.cur_dir == None:
                self.cur_vel = round(random.randint(0, 10)/10)
                self.cur_dir = round(random.randint(-10, 10)/10)
                self.cur_vel_frames_count = True
            if self.cur_vel_frames >= 30:
                self.cur_vel = round(random.randint(0, 10)/10)
                self.cur_dir = round(random.randint(-10, 10)/10)
                self.cur_vel_frames = 0
        else:
            if self.dest.circ_surf.get_rect(topleft=self.dest.pos).colliderect(self.rect):
                pass
            else:
                self.dest.hunted = False
                self.dest = None
                return
            food_exist = False
            for being in ecosys.beings:
                if being == self.dest:
                    food_exist = True
                if hasattr(being, "mask"):
                    if being.mask.overlap(self.mask, (self.pos[0]-being.pos[0], self.pos[1]-being.pos[1])) == None:
                        pass
                    else:
                        self.dest = being
                        food_exist = True
                        break
            if not food_exist:
                self.dest = None
                return
            if self.pos[0]-self.dest.pos[0] > 0:
                self.pos[0]-=((self.speed*1))
            else:
                self.pos[0]+=(self.speed*1)
            if self.pos[1]-self.dest.pos[1] > 0:
                self.pos[1]-=((self.speed*1))
            else:
                self.pos[1]+=(self.speed*1)
            if hasattr(self.dest, "mask"):
                if self.dest.mask.overlap(self.mask, (self.pos[0]-self.dest.pos[0], self.pos[1]-self.dest.pos[1])) == None:
                            pass
                else:
                    self.en += self.dest.en
                    self.dest.en = -100
                    self.dest = None
                    return
        win.blit(self.circ_surf, self.pos)
        if not hasattr(self, "mask"):
            self.mask = pygame.mask.from_surface(self.circ_surf)
        if self.pos[0] in [nu for nu in range(0, win_size[0])] and self.pos[1] in [nu_ for nu_ in range(0, win_size[1])]:
            if self.cur_vel != None and self.dest == None:
                self.pos[self.cur_vel]+=((self.speed*1)*self.cur_dir)
        else:
            if self.pos[0] < 0:
                self.pos[0] = 0
            if self.pos[1] < 0:
                self.pos[1] = 0
            if self.pos[0] > win_size[0]:
                self.pos[0] = win_size[0]
            if self.pos[1] > win_size[1]:
                self.pos[1] = win_size[1]