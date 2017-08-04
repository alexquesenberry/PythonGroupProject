import pygame
from scores import Scores
from game import BLACK

class ScoresScreen(object):
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                running = self.draw()
                if running == False:
                    break
        return running

    def draw(self):

        cursor = Scores()
        topten = cursor.get_top_ten_scores()

        background = pygame.image.load("res/background_main.jpg").convert()
        self.screen.blit(background, [0, 0])

        mouse = pygame.mouse.get_pos()
        release = pygame.mouse.get_pressed()
        if (self.width/2 - 75) < mouse[0] < (self.width/2 + 75) and 700 < mouse[1] < 750:
            pygame.draw.rect(self.screen, (220, 40, 55), (self.width/2 - 75, 700, 150, 50))
            if release[0] == 1:
                print 'click'
                return False
        else:
            pygame.draw.rect(self.screen, (163, 40, 55), (self.width/2 - 75, 700, 150, 50))

        pygame.font.init()
        myfont = pygame.font.SysFont("monospace", 72)
        hslabel = myfont.render("HIGHSCORES", 1, BLACK)
        myfont = pygame.font.SysFont("monospace", 24)
        bcklabel = myfont.render("BACK", 1, (0,0,0))
        text_rect = hslabel.get_rect(center=(self.width/2, 30))

        self.screen.blit(hslabel, text_rect)
        self.screen.blit(bcklabel, (self.width/2 - 33, 715))

        pygame.draw.line(self.screen, BLACK, (0,60),(600,60), 5)

        top = 100
        labels = []
        i = 0
        j = len(topten)
        myfont = pygame.font.SysFont("monospace", 32)
        for record in topten:
            labels.insert(i,myfont.render('{0}.{1: <55s}{2: >10s}'.format(i+1, str(record[1]).strip(), str(record[0]).strip()).replace(" ", "."), 0, BLACK))
            i = i + 1

        for label in labels:
            self.screen.blit(label, (50, top))
            top = top + 35

        pygame.display.flip()

        return True
