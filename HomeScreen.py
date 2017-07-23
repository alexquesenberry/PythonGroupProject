'''
module @HomeScreen.py
description:
 This will serve as the main module for the game
 All the game sequences and parts will be loaded through
 this module
'''
from __future__ import print_function
from LevelScreen import LevelScreen
import pygame
import game


BUTTON_COLOR = (163, 40, 55)
BUTTON_HOVER = (220, 40, 55)
BUTTON_TEXT_COLOR = (26, 255, 26)
WIDTH = 600
HEIGHT = 800
CENTER_SCREEN = (WIDTH / 2)




class HomeScreen(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.view = 0



    def run(self):
        game_loop = True
        while game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #HOME SCREEN
            if self.view == 0:
                self.Add_Background()
                self.Add_Title()
                self.Add_Buttons()
                self.Add_Text_Buttons()
            
            #LEVEL VIEW
            elif self.view == 1:
                self.screen.fill((0, 0, 0))
                x = level.add_home_button()
                self.set_view(x)

            pygame.display.flip()
            self.clock.tick(60)

    #change the view based on number
    def set_view(self, num):
        self.view = num

    def Button_Play(self):
        print("button play clicked")
        click_sound.play()


    def Button_Levels(self):
        print("button levels clicked")
        click_sound.play()
        game.set_view(1) #setting to Level View

    def Button_Extreme(self):
        print("button extreme clicked")
        click_sound.play()

    def Button_Scores(self):
        print("button scores clicked")
        click_sound.play()

    def Button_Exit(self):
        print("button exit clicked")
        pygame.quit()
        quit()


    def Add_Buttons(self):
        mouse = pygame.mouse.get_pos()
        release = pygame.mouse.get_pressed()
        if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 300 < mouse[1] < 350:
            pygame.draw.rect(screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 300, 150, 50))
            if release[0] == 1:
                self.Button_Play()
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 300, 150, 50))

        if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 400 < mouse[1] < 450:
            pygame.draw.rect(screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 400, 150, 50))
            if release[0] == 1:
                self.Button_Levels()
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 400, 150, 50))

        if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 500 < mouse[1] < 550:
            pygame.draw.rect(screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 500, 150, 50))
            if release[0] == 1:
                self.Button_Extreme()
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 500, 150, 50))

        if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 600 < mouse[1] < 650:
            pygame.draw.rect(screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 600, 150, 50))
            if release[0] == 1:
                self.Button_Scores()
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 600, 150, 50))

        if CENTER_SCREEN - 75 < mouse[0] < CENTER_SCREEN + 75 and 700 < mouse[1] < 750:
            pygame.draw.rect(screen, BUTTON_HOVER, (CENTER_SCREEN - 75, 700, 150, 50))
            if release[0] == 1:
                self.Button_Exit()
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, (CENTER_SCREEN - 75, 700, 150, 50))
    #END ADD_BUTTONS

    def Add_Text_Buttons(self):
        my_font = pygame.font.SysFont("monospace", 24, bold = True)
        label1 = my_font.render("PLAY NOW", 1, BUTTON_TEXT_COLOR)
        label2 = my_font.render("LEVELS", 1, BUTTON_TEXT_COLOR)
        label3 = my_font.render("EXTREME", 1, BUTTON_TEXT_COLOR)
        label4 = my_font.render("TOP SCORES", 1, BUTTON_TEXT_COLOR)
        label5 = my_font.render("EXIT", 1, BUTTON_TEXT_COLOR)
        self.screen.blit(label1, (CENTER_SCREEN - 52, 315)) #play now
        self.screen.blit(label2, (CENTER_SCREEN - 40, 415)) #levels
        self.screen.blit(label3, (CENTER_SCREEN - 50, 515)) #extreme play mode
        self.screen.blit(label4, (CENTER_SCREEN - 67, 615)) #scores
        self.screen.blit(label5, (CENTER_SCREEN - 33, 715)) #exit
    #END ADD_TEXT_BUTTONS

    def Add_Title(self):
        myfont = pygame.font.Font("res/FFF_font.ttf", 88)
        label = myfont.render("BrickBreaker", 1, BUTTON_TEXT_COLOR)
        self.screen.blit(label, (1, 50))

    def Add_Background(self):
        self.screen.blit(main_background, [0, 0])        
    #END HOMESCREEN





if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    click_sound = pygame.mixer.Sound("res/beep5.mps")
    pygame.mixer.music.load("res/background_music.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("BRICK BREAKER")
    main_background = pygame.image.load("res/background_main.jpg").convert() #load background image
    game = HomeScreen(screen)
    level = LevelScreen(screen)
    game.run()