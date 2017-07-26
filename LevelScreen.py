'''
module@ LevelsScreen.py
'''

import pygame
BLACK = (0, 0, 0)
BUTTON_COLOR = (163, 40, 55)
BUTTON_HOVER = (220, 40, 55)
BUTTON_TEXT_COLOR = (26, 255, 26)
WIDTH = 600
HEIGHT = 800
CENTER_SCREEN = (WIDTH / 2)




class LevelScreen(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))

    def add_home_button(self):
    	my_font = pygame.font.SysFont("monospace", 24, bold = True)
    	mouse = pygame.mouse.get_pos()
        release = pygame.mouse.get_pressed()
    	if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 700 < mouse[1] < 750:
            pygame.draw.rect(self.screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 700, 150, 50))
            if release[0] == 1:
        	    return 0
        else:
            pygame.draw.rect(self.screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 700, 150, 50))
    
        back_button = my_font.render("HOME", 1, BUTTON_TEXT_COLOR)
        self.screen.blit(back_button, (CENTER_SCREEN - 33, 715))
        return 1   #keep screen displayed 