import pygame, sys, pygame_textinput
import random
if __import__("sys").platform == "emscripten":
    import platform
pygame.init()
global web
web = True
global cursor_mask
global cursor_img
if not web:
    cursor_img = pygame.image.load("assets\Spritesheets\\cursor.png")
else:
    cursor_img = pygame.image.load("assets/Spritesheets//cursor.png")
cursor_mask = pygame.mask.from_surface(cursor_img)
global gene_dict
gene_dict = {"speed":0, "energy":1, "size":2, "color":3}
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
global win_size
win_size = [win.get_width(), win.get_height()]
pygame.display.set_caption("Dynasty")
global def_frame
def_frame = 60
def blit_center(img):
    win.blit(img, [win_size[0]/2-(img.get_width()/2), win_size[1]/2-(img.get_height()/2)])
def center_pos(img):
    return [win_size[0]/2-(img.get_width()/2), win_size[1]/2-(img.get_height()/2)]
def swap_color(img, col1, col2):
    pygame.transform.threshold(img ,img ,col1, (10, 10, 10), col2, 1, None, True)
def scale_image(img, factor=8.0):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size).convert()
class SpriteSheet:
    def __init__(self, sheet, size, colorkey = [0, 0, 0]):
        self.spritesheet = sheet
        self.colorkey = colorkey
        self.size = [self.spritesheet.get_width()/size[0], self.spritesheet.get_height()/size[1]]
        self.sheet = []
        for i in range(size[1]):
            self.sheet.append([])
            for j in range(size[0]):
                image = pygame.Surface((self.size))
                image.set_colorkey(self.colorkey)
                image.blit(self.spritesheet, (0, 0), [j*self.size[0], i*self.size[1], self.size[0], self.size[1]])
                self.sheet[i].append(image)
    def get(self, loc):
        return self.sheet[loc[1]][loc[0]]

