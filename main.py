from assets.scripts.ecology import *
global ecosystem
ecosystem = EcoSytem([10, 2, 50, True])
global screen
screen = 1
ui_font = pygame.font.Font("PrinceValiant.ttf", 90)
b_font = pygame.font.Font("PrinceValiant.ttf", 64)
title = ui_font.render("Dynasty", False, (255, 202, 24))
start = b_font.render("Start", False, (255, 255, 255))
death = b_font.render("Restart", False, (255, 255, 255))
back_ = b_font.render("Menu", False, (255, 255, 255))
b = b_font.render("Herbivores", False, (255, 255, 255))
h = b_font.render("Carnivores", False, (255, 255, 255))
f = b_font.render("Food", False, (255, 255, 255))
i = b_font.render("Player", False, (255, 255, 255))
e = b_font.render("Exit", False, (255, 255, 255))
title_pos = [center_pos(title)[0], center_pos(title)[1]/2]
being_input = TextInputVisualizer(TextInputManager(validator=lambda input: ( len(input) <= 2 and input in [str(num_) for num_ in range(1, 100)]+[""])))
being_input.cursor_visible = True
being_input.cursor_color = (255, 255, 255)
being_input.font_color = (255, 255, 255)
being_input.font_object = b_font
hunter_input = TextInputVisualizer(TextInputManager(validator=lambda input: ( len(input) <= 2 and input in [str(num_) for num_ in range(1, 100)]+[""])))
hunter_input.cursor_visible = True
hunter_input.cursor_color = (255, 255, 255)
hunter_input.font_color = (255, 255, 255)
hunter_input.font_object = b_font
food_input = TextInputVisualizer(TextInputManager(validator=lambda input: ( len(input) <= 2 and input in [str(num_) for num_ in range(1, 100)]+[""])))
food_input.cursor_visible = True
food_input.cursor_color = (255, 255, 255)
food_input.font_color = (255, 255, 255)
food_input.font_object = b_font
i_input = TextInputVisualizer(TextInputManager(validator=lambda input: ( len(input) <= 1 and input in ["y", "n", "Y", "N", ""])))
i_input.cursor_visible = True
i_input.cursor_color = (255, 255, 255)
i_input.font_color = (255, 255, 255)
i_input.font_object = b_font
inputs = [being_input.surface.get_rect(topleft=[center_pos(title)[0]+20, center_pos(title)[1]/0.75]), hunter_input.surface.get_rect(topleft=[center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+100]), food_input.surface.get_rect(topleft=[center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+200]), i_input.surface.get_rect(topleft=[center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+300])]
pygame.key.set_repeat(200, 25)
def play(args):
    global screen
    screen = 2
    final = [10, 2, 50, True]
    global ecosystem
    if being_input.value == "" and hunter_input.value == "" and food_input.value == "":
        pass
    if being_input.value != "":
        final[0] = int(being_input.value)
    if hunter_input.value != "":
        final[1] = int(hunter_input.value)
    if food_input.value != "":
        final[2] = int(food_input.value)
    if i_input.value != "":
        if final[3] in ["y", "Y"]:
            final[3] = True
        else:
            final[3] = False
    ecosystem = EcoSytem(final)
def back(args):
    global screen
    screen = 1
def ex(args):
    sys.exit()
buttons = [Button([center_pos(title)[0]+20, center_pos(title)[1]/1.25], [scale_image(pygame.image.load("start_unpressed.png")), scale_image(pygame.image.load("start_pressed.png"))], [play, []]), Button([center_pos(title)[0]+20, (center_pos(title)[1]/1.25)+100], [scale_image(pygame.image.load("start_unpressed.png")), scale_image(pygame.image.load("start_pressed.png"))], [ex, []])]
death_button = Button([center_pos(title)[0]+20, center_pos(title)[1]*1.25], [scale_image(pygame.image.load("start_unpressed.png")), scale_image(pygame.image.load("start_pressed.png"))], [play, []])
back_button = Button([center_pos(title)[0]+20, center_pos(title)[1]*1.5], [scale_image(pygame.image.load("start_unpressed.png")), scale_image(pygame.image.load("start_pressed.png"))], [back, []])
run = True
bg = pygame.image.load("bg.png").convert()
while run:
    num = -1
    win.fill((0, 0, 0))
    if screen == 2:
        ecosystem.update()
        if ecosystem.is_interactive:
            player = [p for p in ecosystem.beings if p.auto == False]
            if len(player) == 0:
                blit_center(ecosystem.death_text)
                death_button.update()
                win.blit(death, [death_button.pos[0]+35, death_button.pos[1]+13+(8*death_button.current)])
                back_button.update()
                win.blit(back_, [back_button.pos[0]+50, back_button.pos[1]+13+(8*back_button.current)])
    else:
        win.blit(bg, (0, 0))
        win.blit(title, title_pos)
        for button in buttons:
            num += 1
            button.update()
        win.blit(start, [buttons[0].pos[0]+55, buttons[0].pos[1]+13+(8*buttons[0].current)])
        win.blit(e, [buttons[1].pos[0]+70, buttons[1].pos[1]+13+(8*buttons[1].current)])
        if inputs[0].collidepoint(pygame.mouse.get_pos()):
            being_input.update(pygame.event.get())

        elif inputs[1].collidepoint(pygame.mouse.get_pos()):
            hunter_input.update(pygame.event.get())

        elif inputs[2].collidepoint(pygame.mouse.get_pos()):
            food_input.update(pygame.event.get())
        elif inputs[3].collidepoint(pygame.mouse.get_pos()):
            i_input.update(pygame.event.get())
        for i__ in inputs:
            i__.w = title.get_width()
            pygame.draw.rect(win, (45, 45, 45), i__)   
        
        win.blit(being_input.surface, [center_pos(title)[0]+20, center_pos(title)[1]/0.75])
        if being_input.value == "":
            win.blit(b, [center_pos(title)[0]+20, center_pos(title)[1]/0.75])
        win.blit(hunter_input.surface, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+100])
        if hunter_input.value == "":
            win.blit(h, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+100])
        win.blit(food_input.surface, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+200])
        if food_input.value == "":
            win.blit(f, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+200])
        win.blit(i_input.surface, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+300])
        if i_input.value == "":
            win.blit(i, [center_pos(title)[0]+20, (center_pos(title)[1]/0.75)+300])
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        screen = 1
    pygame.display.update()
pygame.quit()
sys.exit()
