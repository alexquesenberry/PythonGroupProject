#WIDTH = 1280
#HEIGHT = 800
from __future__ import print_function
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
BLUE = (0, 0, 255)
YELLOW = (237, 249, 57)
PURPLE = (189, 26, 221)




#window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#pygame.display.set_caption('Brick Break')


def init(width, height):
	global fps
	global pad, score
	global BALL_RADIUS, PAD_WIDTH, PAD_HEIGHT
	global WIDTH, HEIGHT


	WIDTH = width
	HEIGHT = height



	debug = False

	BALL_RADIUS = math.sqrt(WIDTH*HEIGHT)
	PAD_WIDTH = WIDTH/5
	PAD_HEIGHT = HEIGHT/50
	score=0

	pygame.init()
	fps = pygame.time.Clock()

	pad = bb_objs.paddle(WIDTH/2, HEIGHT-HEIGHT/15, PAD_WIDTH, PAD_HEIGHT, GREEN)
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
	#init_vel = [-WIDTH/100, -HEIGHT/250]
	init_vel = [0, 0]
	#if len(balls) > 0:
	#	balls.pop()
	balls.append(bb_objs.ball(WIDTH/2 - PAD_WIDTH/6, HEIGHT/2, init_vel, PAD_WIDTH/15, SILVER))
	#balls.append(bb_objs.ball(WIDTH/4,  HEIGHT-HEIGHT/15, init_vel, PAD_WIDTH/15, SILVER))	#Test Ball
	
	

def keydown(event):
	global pad
	if event.key == K_LEFT:
		pad.vel += -WIDTH/(WIDTH/6)
	elif event.key == K_RIGHT:
		pad.vel += WIDTH/(WIDTH/6)
		
	if debug == True:	
		#print("Pad Velocity:",pad.vel)
		None


def keyup(event):
	global pad

	if event.key == K_LEFT:
		pad.vel += WIDTH/(WIDTH/6)
		if balls[0].vel[0] == 0 and balls[0].vel[1] == 0:
			balls[0].vel[1] = HEIGHT/200

	if event.key == K_RIGHT:
		pad.vel += -WIDTH/(WIDTH/6)
		if balls[0].vel[0] == 0 and balls[0].vel[1] == 0:
			balls[0].vel[1] = HEIGHT/200
	
	if event.key == K_SPACE:
		if balls[0].vel[0] == 0 and balls[0].vel[1] == 0:
			balls[0].vel[1] = HEIGHT/200


	if debug == True:
		#print(pad.vel)
		None


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
	if pad.pos[0] > PAD_WIDTH/2 + WIDTH/20 and pad.pos[0] < WIDTH - PAD_WIDTH/2 - WIDTH/20:	#Center Movement
		pad.pos[0] += pad.vel
	elif pad.pos[0] <= PAD_WIDTH/2 + WIDTH/20 and pad.vel > 0:	#Left Bound
		pad.pos[0] += pad.vel
	elif pad.pos[0] >= WIDTH - PAD_WIDTH/2 - WIDTH/20 and pad.vel < 0:	#Right Bound
		pad.pos[0] += pad.vel


	# Draws Balls
	pygame.draw.circle(canvas, SILVER, balls[0].pos, balls[0].radius, 0)

	i = 0	#replace with for loop, that iterates all over balls list
	# Update Ball
	balls[i].pos[0] += int(balls[i].vel[0])
	balls[i].pos[1] += int(balls[i].vel[1])
	vel_vect = (balls[i].vel[0]**2 + balls[i].vel[1]**2)**(0.5)
	if vel_vect < 4:
		vel_vect = 4
	elif vel_vect > 8:
		vel_vect = 8
		
	

	# Wall Collision 
	if balls[i].pos[0] <= WIDTH/20 + balls[i].radius:	# left
		balls[i].vel[0] = -balls[i].vel[0]
	if balls[i].pos[0] >= WIDTH - WIDTH/20:			# right
		balls[i].vel[0] = -balls[i].vel[0]
	if balls[i].pos[1] <= HEIGHT/10 + balls[i].radius:	# top
		balls[i].vel[1] = -balls[i].vel[1]

	# Pad Collision
	if (balls[i].pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and balls[i].pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (balls[i].pos[0] >= pad.pos[0] - PAD_WIDTH/2 and balls[i].pos[0] <= pad.pos[0] + PAD_WIDTH/2):	# Hits Top of Pad
		balls[i].pos[1] = pad.pos[1] - PAD_HEIGHT/2
		if debug == True:
			contact_frac = (float(balls[i].pos[0]) - float(pad.pos[0]))/(PAD_WIDTH)

#
# cos(-) = ball_pos - pad_pos / (pad_width/2) = angle of deflection
# sin(AoD) * vel_vec = Y_vel
# cos(AoD) * vel_vec = X_vel



			if contact_frac > 0:
				balls[i].vel[1] = -math.sin(math.pi * contact_frac) * vel_vect * 1.05
				balls[i].vel[0] = math.cos(math.pi * contact_frac) * vel_vect * 1.05
			elif contact_frac < 0:
				balls[i].vel[1] = math.sin(math.pi * contact_frac) * vel_vect * 1.05
				balls[i].vel[0] = -math.cos(math.pi * contact_frac) * vel_vect * 1.05
			elif contact_frac == 0:
				balls[i].vel[1] = -vel_vect * 1.05
				#balls[i].vel[0] = 0



			print(contact_frac)
			print(math.sin(math.pi * contact_frac), math.cos(math.pi * contact_frac), sep=' : ')
			print('X:',balls[i].vel[0], '\tY:', balls[i].vel[1], '\tVec:', vel_vect)
			#print('X:', math.sin(math.pi * contact_frac))
			#print('Y:', math.cos(math.pi * contact_frac))
		else: 
			balls[i].vel[1] = -balls[i].vel[1]

	# Pad Buffers
	elif (balls[i].pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and balls[i].pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (balls[i].pos[0] >= pad.pos[0] - PAD_WIDTH/2 - math.fabs(balls[i].vel[0])*3 + pad.vel and balls[i].pos[0] <= pad.pos[0] - PAD_WIDTH/2):	# Hits Side of Pad Left
		balls[i].vel[0] = -balls[i].vel[0]
		balls[i].vel[1] = 5
		if debug == True:
			print("hit left")
	elif (balls[i].pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and balls[i].pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (balls[i].pos[0] >= pad.pos[0] + PAD_WIDTH/2 and balls[i].pos[0] <= pad.pos[0] + PAD_WIDTH/2 + math.fabs(balls[i].vel[0])*3):	# Hits Side of Pad Left
		balls[i].vel[0] = -balls[i].vel[0]
		balls[i].vel[1] = 5
		if debug == True:
			print("hit right")
	
	# Ball Death
	if balls[i].pos[1] >= HEIGHT: #Misses Pad
		ball_init()
		pad.pos = [WIDTH/2, HEIGHT-HEIGHT/15]
		if debug == True:
			print("DEAD")
		



		# Hit box displays
	if debug == True:
		# Pad
		pygame.draw.line(canvas, WHITE, [0, pad.pos[1] - PAD_HEIGHT/2], [WIDTH, pad.pos[1] - PAD_HEIGHT/2], 1) # Above
		pygame.draw.line(canvas, WHITE, [0, pad.pos[1] + PAD_HEIGHT/2], [WIDTH, pad.pos[1] + PAD_HEIGHT/2], 1) # Bottom
		pygame.draw.line(canvas, WHITE, [pad.pos[0] - PAD_WIDTH/2, 0], 	[pad.pos[0] - PAD_WIDTH/2, HEIGHT], 1) # Left Side
		pygame.draw.line(canvas, WHITE, [pad.pos[0] + PAD_WIDTH/2, 0], 	[pad.pos[0] + PAD_WIDTH/2, HEIGHT], 1) # Right Side

		# Pad Buffer
		pygame.draw.line(canvas, BLUE, 	[pad.pos[0] - PAD_WIDTH/2 - math.fabs(balls[i].vel[0])*3,0], [pad.pos[0] - PAD_WIDTH/2 - math.fabs(balls[i].vel[0])*3,HEIGHT] , 1) # Left
		pygame.draw.line(canvas, BLUE, 	[pad.pos[0] + PAD_WIDTH/2 + math.fabs(balls[i].vel[0])*3,0], [pad.pos[0] + PAD_WIDTH/2 + math.fabs(balls[i].vel[0])*3,HEIGHT] , 1) # Right

		# Ball
		pygame.draw.line(canvas, WHITE, [balls[i].pos[0], 0], [balls[i].pos[0], HEIGHT] , 1) # Vertical
		pygame.draw.line(canvas, WHITE, [0, balls[i].pos[1]], [WIDTH, balls[i].pos[1]] , 1) # Horizontal




if __name__ == "__main__":

	width = 600
	height = 800
	window = pygame.display.set_mode((width, height), 0, 32)
	pygame.display.set_caption('Brick Break')
	init(width,height)
	debug = True
	run(window)


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
