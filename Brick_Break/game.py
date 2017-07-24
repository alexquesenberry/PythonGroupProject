#WIDTH = 1280
#HEIGHT = 800

import random
import pygame, sys
import math
import bb_objs
from pygame.locals import *

#pygame.init()
#fps = pygame.time.Clock()

#color palette 
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
SILVER = (192, 192, 192)



#BALL_RADIUS = math.sqrt(WIDTH*HEIGHT)
#PAD_WIDTH = WIDTH/10
#PAD_HEIGHT = HEIGHT/50
#HALF_PAD_WIDTH = PAD_WIDTH/2
#HALF_PAD_HEIGHT = PAD_HEIGHT/2
#score=0

#window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#pygame.display.set_caption('Brick Break')


def init(width, height):
	global fps
	global pad, score
	global BALL_RADIUS, PAD_WIDTH, PAD_HEIGHT
	global WIDTH, HEIGHT

	WIDTH = width#1280
	HEIGHT = height#800

	BALL_RADIUS = math.sqrt(WIDTH*HEIGHT)
	PAD_WIDTH = WIDTH/10
	PAD_HEIGHT = HEIGHT/50
	score=0

	pygame.init()
	fps = pygame.time.Clock()

	pad = bb_objs.paddle(WIDTH/2, HEIGHT-HEIGHT/15, WIDTH/10, HEIGHT/50, GREEN)
	score = 0
	ball_init()
	#run()

def run(window):

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

def ball_init():
	global balls
	balls = []
	init_vel = [-WIDTH/100, -HEIGHT/250]
	balls.append(bb_objs.ball(WIDTH/2, HEIGHT/2, init_vel, PAD_WIDTH/15, SILVER))

	
	

def keydown(event):
	global pad
	if event.key == K_LEFT:
		pad.vel += -WIDTH/(WIDTH/6)
	elif event.key == K_RIGHT:
		pad.vel += WIDTH/(WIDTH/6)
		
	#print(pad.vel)


def keyup(event):
	global pad

	if event.key == K_LEFT:
		pad.vel += WIDTH/(WIDTH/6)
	if event.key == K_RIGHT:
		pad.vel += -WIDTH/(WIDTH/6)
		
	#print(pad.vel)


def draw(canvas):

	global pad, balls, score

	canvas.fill(BLACK)
	
	# Drawns the white borders
	pygame.draw.line(canvas, RED, [WIDTH, 0], [WIDTH, HEIGHT], WIDTH/10) #right
	pygame.draw.line(canvas, RED, [0, 0], [0, HEIGHT], WIDTH/10) #left
	pygame.draw.line(canvas, RED, [0, 0], [WIDTH, 0], HEIGHT/5) #top

	# Draws Paddle
	pygame.draw.polygon(canvas, GREEN, [	[pad.pos[0] - PAD_WIDTH/2, pad.pos[1] - PAD_HEIGHT/2], 
						[pad.pos[0] - PAD_WIDTH/2, pad.pos[1] + PAD_HEIGHT/2], 
						[pad.pos[0] + PAD_WIDTH/2, pad.pos[1] + PAD_HEIGHT/2], 
						[pad.pos[0] + PAD_WIDTH/2, pad.pos[1] - PAD_HEIGHT/2]], 0)
	# Update paddle position
	if pad.pos[0] > PAD_WIDTH/2 + WIDTH/20 and pad.pos[0] < WIDTH - PAD_WIDTH/2 - WIDTH/20:
		pad.pos[0] += pad.vel
	elif pad.pos[0] == PAD_WIDTH/2 + WIDTH/20 and pad.vel > 0:
		pad.pos[0] += pad.vel
	elif pad.pos[0] == WIDTH - PAD_WIDTH/2 - WIDTH/20 and pad.vel < 0:
		pad.pos[0] += pad.vel

	# Draws Ball
	pygame.draw.circle(canvas, SILVER, balls[0].pos, balls[0].radius, 0)

	i = 0	#replace with for loop, that iterates all over balls list
	# Update Ball
	balls[i].pos[0] += balls[i].vel[0]
	balls[i].pos[1] += balls[i].vel[1]

	# Wall Collision 
	if balls[i].pos[0] <= WIDTH/20 + balls[i].radius:	# left
		balls[i].vel[0] = -balls[i].vel[0]
	if balls[i].pos[0] >= WIDTH - WIDTH/20:			# right
		balls[i].vel[0] = -balls[i].vel[0]
	if balls[i].pos[1] <= HEIGHT/10 + balls[i].radius:	# top
		balls[i].vel[1] = -balls[i].vel[1]

	

	


if __name__ == "__main__":

	init()
"""
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
"""
