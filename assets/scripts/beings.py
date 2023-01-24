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
        self.auto = True
        self.sighted_food = False
        self.speed = round(self.genes[gene_dict["speed"]]/6)
        self.en = 0.5
        self.radius = round(self.genes[gene_dict["size"]]/10)
        self.color = self.genes[gene_dict["color"]]
    def update(self, ecosys):
        self.en -= (0.0015/5)
        if self.speed <= 0:
            self.speed = 2
        self.rect = pygame.Rect(self.pos[0]-self.radius*3, self.pos[1]-self.radius*3, self.radius*8, self.radius*8)
        #pygame.draw.rect(win, (255, 0, 0), self.rect)
        if self.en <= 0:
            ecosys.beings = [b for b in ecosys.beings if b != self]
            #print("ded")
            del self
            return
        if self.auto:
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
        if not self.auto:
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                self.pos[0]-=((self.speed*1))
                print("l")
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.pos[0]+=(self.speed*1)
                print("r")
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                self.pos[1]-=((self.speed*1))
                print('u')
            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                self.pos[1]+=(self.speed*1)
                print('d')
        if not hasattr(self, "circ_surf"):
            if not self.auto:
                ecosys.gen_num += 1
            self.you_text = ecosys.font.render("YOU"+"_"+str(ecosys.gen_num), False, (255, 202, 24))
            self.circ_surf = pygame.Surface((self.radius*2, self.radius*2))
            pygame.draw.circle(self.circ_surf, self.color, (self.radius, self.radius), self.radius)
            self.circ_surf.set_colorkey((0, 0, 0))
            self.mask = pygame.mask.from_surface(self.circ_surf)
        win.blit(self.circ_surf, self.pos)
        if not self.auto:
            win.blit(self.you_text, [self.pos[0], self.pos[1]-20])
            win.blit(ui_f.render("Energy"+": "+str(self.en), False, (255, 202, 24)), [100, 50])
            if round(self.en) >= 3:
                win.blit(ui_f.render("You can reproduce!", False, (255, 202, 24)), [100, 150])
            else:
                win.blit(ui_f.render("You need more energy to reproduce", False, (255, 202, 24)), [100, 150])
            win.blit(ui_f.render("Speed"+": "+str(self.speed), False, (255, 202, 24)), [100, 250])
            win.blit(ui_f.render("Radius (Size)"+": "+str(self.radius), False, (255, 202, 24)), [100, 350])
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
        if not ecosys.is_interactive:
            if self.circ_surf.get_rect(topleft=self.pos).collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    if self.auto:
                        self.auto = False
                        if not self.auto:
                            ecosys.gen_num += 1
                        self.you_text = ecosys.font.render("YOU"+"_"+str(ecosys.gen_num), False, (255, 202, 24))
                        for being in ecosys.beings:
                            if being != self:
                                being.auto = True
                        return
            if not self.auto:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.auto = True