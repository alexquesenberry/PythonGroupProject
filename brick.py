import pygame
import random as rand

brick_colors = ["Red", "Blue", "Green", "Cyan", "Magenta", "Yellow"]

class Brick(object):
    """Brick class module"""

    def __init__(self, durability, pos, can_dim):
        self.durability = durability
        self.pos = pos
        self.img_arry = []
        self.hit = 0

        pygame.display.set_mode(can_dim)
        self.init_imgs(rand.randint(0, 5))
        self.img = self.img_arry[0]

    def init_imgs(self, rand_int):
        color = brick_colors[rand_int]
        self.img_arry.append(pygame.image.load("bricks/plain" + color + ".png").convert_alpha())
        if self.durability > 1:
            self.img_arry.append(pygame.image.load("bricks/onehit" + color + ".png").convert_alpha())
        if self.durability > 2:
            self.img_arry.append(pygame.image.load("bricks/twohit" + color + ".png").convert_alpha())

    def set_brick(self, index):
        """sets the current brick"""
        self.img = self.img_arry[index]

    def draw_brick(self, can):
        """draws the current brick to the can passed in"""
        can.blit(self.img, self.pos)

    def increase_hit(self):
        """increase the hit counter set appropriate brick"""
        self.hit += 1
        if self.hit < self.durabilty:
            self.set_brick(self.hit)
        
