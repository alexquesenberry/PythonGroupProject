import random
import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
SILVER = (192, 192, 192)


WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = WIDTH/10
PAD_HEIGHT = HEIGHT/50
HALF_PAD_WIDTH = PAD_WIDTH/2
HALF_PAD_HEIGHT = PAD_HEIGHT/2
ball_pos = [0,0]
ball_vel = [0,0]
paddle_vel = 0
score=0
r_score = 0

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')


def init():
	global paddle_pos, paddle_vel, score, r_score
	global score1, score2

	paddle_pos = [WIDTH/2, HEIGHT-HEIGHT/15]
	score = 0
	r_score = 0
	ball_init()

def ball_init():
	global ball_pos, ball_vel
	ball_pos = [WIDTH/2, HEIGHT/2]
	

def keydown(event):
	global paddle_vel

	if event.key == K_LEFT:
		paddle_vel = -8
	elif event.key == K_RIGHT:
		paddle_vel = 8
	elif event.key == K_w:
		paddle_vel = -8
	elif event.key == K_s:
		paddle_vel = 8

def keyup(event):
	global paddle_vel

	if event.key in (K_w, K_s):
		paddle_vel = 0
	elif event.key in (K_LEFT, K_RIGHT):
		paddle_vel = 0


def draw(canvas):

	global paddle_pos, ball_pos, ball_vel, score, r_score

	canvas.fill(BLACK)
	
	# Drawns the white borders
	pygame.draw.line(canvas, RED, [WIDTH, 0], [WIDTH, HEIGHT], WIDTH/10) #right
	pygame.draw.line(canvas, RED, [0, 0], [0, HEIGHT], WIDTH/10) #left
	pygame.draw.line(canvas, RED, [0, 0], [WIDTH, 0], HEIGHT/5) #top

	# Draws Paddle
	pygame.draw.polygon(canvas, GREEN, [	[paddle_pos[0] - HALF_PAD_WIDTH, paddle_pos[1] - HALF_PAD_HEIGHT], 
						[paddle_pos[0] - HALF_PAD_WIDTH, paddle_pos[1] + HALF_PAD_HEIGHT], 
						[paddle_pos[0] + HALF_PAD_WIDTH, paddle_pos[1] + HALF_PAD_HEIGHT], 
						[paddle_pos[0] + HALF_PAD_WIDTH, paddle_pos[1] - HALF_PAD_HEIGHT]], 0)

	# Draws Ball
	pygame.draw.circle(canvas, SILVER, ball_pos, PAD_WIDTH/15, 0)

	
	# Update paddle position
	if paddle_pos[0] > HALF_PAD_WIDTH + WIDTH/20 and paddle_pos[0] < WIDTH - HALF_PAD_WIDTH - WIDTH/20:
		paddle_pos[0] += paddle_vel
	elif paddle_pos[0] == HALF_PAD_WIDTH + WIDTH/20 and paddle_vel > 0:
		paddle_pos[0] += paddle_vel
	elif paddle_pos[0] == WIDTH - HALF_PAD_WIDTH - WIDTH/20 and paddle_vel < 0:
		paddle_pos[0] += paddle_vel




init()

while True:

	draw(window)

	for event in pygame.event.get():
	
		if event.type == KEYDOWN:
			keydown(event)
		if event.type == KEYUP:
			keyup(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fps.tick(60)
