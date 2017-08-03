#WIDTH = 1280
#HEIGHT = 800
from __future__ import print_function
import random
import pygame, sys
import math
import bb_objs
from brick import Brick
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
GOLD = (206,184,136)


CLOCK = pygame.time.Clock()

#BALL_RADIUS = math.sqrt(WIDTH*HEIGHT)
#PAD_WIDTH = WIDTH/10
#PAD_HEIGHT = HEIGHT/50
#HALF_PAD_WIDTH = PAD_WIDTH/2
#HALF_PAD_HEIGHT = PAD_HEIGHT/2
score=0
score_multi = 1

#window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
#pygame.display.set_caption('Brick Break')


def init(width, height):
	global fps
	global lives
	global BALL_RADIUS, PAD_WIDTH, PAD_HEIGHT
	global WIDTH, HEIGHT
	global debug
	global bricks, pad
	global BRICK_WIDTH, BRICK_HEIGHT

	WIDTH = width
	HEIGHT = height



	bricks = []
	BRICK_WIDTH = HEIGHT/10
	BRICK_HEIGHT = WIDTH/20

	debug = False

	BALL_RADIUS = math.sqrt(WIDTH*HEIGHT)
	PAD_WIDTH = WIDTH/5
	PAD_HEIGHT = HEIGHT/50
	score=0
	score_multi = 1.0
	lives = 3

	pygame.init()
	fps = pygame.time.Clock()

	pad = bb_objs.paddle(WIDTH/2, HEIGHT-HEIGHT/15, WIDTH/10, HEIGHT/50, GREEN)
	score = 0
	ball_init()
	init_bricks(5)
	#run()


def pause(window):
	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pause = False
				elif event.key == pygame.K_q:
					pygame.quit()
					running = False
					return
					

		MYFONT = pygame.font.Font("res/FFF_font.ttf", 88)
		MYFONT2 = pygame.font.Font("res/FFF_font.ttf", 30)
		label = MYFONT.render("BrickBreaker", 100, RED)
		label2 = MYFONT.render("Paused", 100, RED)
		label3 = MYFONT2.render("press C to continue", 100, RED)
		label4 = MYFONT2.render("press Q to quit", 100 , RED)
		window.blit(label, (1, 50))
		window.blit(label2, (50, 400))
		window.blit(label3, (50, 500))
		window.blit(label4, (50, 550))

		pygame.display.update()
		CLOCK.tick(30)

def game_over(window):
	youLose = True
	while youLose:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()				
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pass
				#HERE WE WANT TO RESTART THE GAME
				elif event.key == pygame.K_q:
					pygame.quit()
					running == False
					return

		MYFONT = pygame.font.Font("res/FFF_font.ttf", 88)
		MYFONT2 = pygame.font.Font("res/FFF_font.ttf", 30)
		label = MYFONT.render("BrickBreaker", 100, RED)
		label2 = MYFONT.render("Game Over", 100, RED)
		label3 = MYFONT2.render("press P to play again", 100, RED)
		label4 = MYFONT2.render("press q to quit", 100, RED)
		label5 = MYFONT2.render("YOUR SCORE: " + str(score), 100, RED)
		window.blit(label, (1, 50))
		window.blit(label2, (50, 400))
		window.blit(label5, (50, 500))
		window.blit(label3, (50, 550))
		window.blit(labelc4, (50, 600))

		pygame.display.update()
		CLOCK.tick(30)




def run(window):
	global running, lives

	running = True
	while running:

		draw(window)

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				keydown(event, window)
			if event.type == KEYUP:
				keyup(event)
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
		if lives == 0:
			game_over(window)

		pygame.display.update()
		fps.tick(60)

def ball_init():
	global balls
	balls = []
	#init_vel = [-WIDTH/100, -HEIGHT/250]
	init_vel = [0, 0]
	if len(balls) > 0:
		balls.pop()
	#balls.append(bb_objs.ball(WIDTH/2 - PAD_WIDTH/8, HEIGHT/2, init_vel, PAD_WIDTH/15, SILVER))
	balls.append(bb_objs.ball(WIDTH/2, HEIGHT-HEIGHT/10, init_vel, PAD_WIDTH/15, SILVER))#Test Ball
	
def init_bricks(colmns):
	"""
	pass in the number of columns
	you want initially drawn		
	"""
	rows = (WIDTH - 2 * WIDTH / 10) / BRICK_WIDTH
	x_offset = WIDTH / 10
	y_offset = HEIGHT / 7

	for i in range(0, colmns):
		for j in range(0, rows):
			bricks.append(Brick(3, [j * 80 + x_offset, i * 30 + y_offset], [WIDTH, HEIGHT]))

def keydown(event, window):
	global pad
	if event.key == K_LEFT:
		pad.vel += -WIDTH/(WIDTH/6)
		if balls[0].vel[1] == 0:
			balls[0].vel[0] = pad.vel
	elif event.key == K_RIGHT:
		pad.vel += WIDTH/(WIDTH/6)
		if balls[0].vel[1] == 0:
			balls[0].vel[0] = pad.vel
	elif event.key == pygame.K_p:
		pause(window)
		
	if debug == True:	
		#print("Pad Velocity:",pad.vel)
		None


def keyup(event):
	global pad

	if event.key == K_LEFT:
		pad.vel += WIDTH/(WIDTH/6)
		if balls[0].vel[1] == 0:
			balls[0].vel[0] = pad.vel
	if event.key == K_RIGHT:
		pad.vel += -WIDTH/(WIDTH/6)
		if balls[0].vel[1] == 0:
			balls[0].vel[0] = pad.vel
	if event.key == K_SPACE:
		if balls[0].vel[0] == 0 and balls[0].vel[1] == 0:
			balls[0].vel[1] = float(-HEIGHT/150)
			balls[0].vel[0] = float(-balls[0].vel[1]/4)

	if debug == True:
		#print(pad.vel)
		None


def draw(canvas):
	global score, score_multi, lives


	canvas.fill(BLACK)

	
	# Drawns the white borders
	pygame.draw.line(canvas, GOLD, [WIDTH, 0], [WIDTH, HEIGHT], WIDTH/10) #right
	pygame.draw.line(canvas, GOLD, [0, 0], [0, HEIGHT], WIDTH/10) #left
	pygame.draw.line(canvas, GOLD, [0, 0], [WIDTH, 0], HEIGHT/5) #top

	# Displays Score
	MYFONT = pygame.font.Font("res/FFF_font.ttf", 30)
	label = MYFONT.render("Score: " + str(score), 100, RED)
	canvas.blit(label, (50, 50))

	MYFONT = pygame.font.Font("res/FFF_font.ttf", 30)
	label2 = MYFONT.render("Lives: " + str(lives), 100, RED)
	canvas.blit(label2, (WIDTH - 150, 45))

	#draws the bricks
	for brk in bricks:
		brk.draw_brick(canvas)

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
	ball = balls[0]	#replace with for loop, that iterates all over balls list
	pygame.draw.circle(canvas, SILVER, ball.pos, ball.radius, 0)

	# Update Ball
	ball.pos[0] += int(ball.vel[0])
	ball.pos[1] += int(ball.vel[1])
	vel_vect = (ball.vel[0]**2 + ball.vel[1]**2)**(0.5)
	if vel_vect < 4:
		vel_vect = 4
	elif vel_vect > 8:
		vel_vect = 8


	# Wall Collision 
	if ball.pos[0] <= WIDTH/20 + ball.radius:	# left
		ball.vel[0] = -ball.vel[0]
	if ball.pos[0] >= WIDTH - WIDTH/20:		# right
		ball.vel[0] = -ball.vel[0]
	if ball.pos[1] <= HEIGHT/10 + ball.radius:	# top
		ball.vel[1] = -ball.vel[1]

	# Pad Collision
	if (ball.pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and ball.pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (ball.pos[0] >= pad.pos[0] - PAD_WIDTH/2 and ball.pos[0] <= pad.pos[0] + PAD_WIDTH/2):	# Hits Top of Pad
		ball.pos[1] = pad.pos[1] - PAD_HEIGHT/2
		
		
		AoD = math.acos((float(ball.pos[0]) - float(pad.pos[0]))/(PAD_WIDTH/2))
		Y_vel = math.sin(AoD) * -vel_vect
		X_vel = math.cos(AoD) * vel_vect


		ball.vel[1] = Y_vel * 1.05
		ball.vel[0] = X_vel * 1.05



		if debug == True:

			#print("%i : %.2f : %.2f : %.2f" % (math.degrees(AoD), X_vel, Y_vel, vel_vect))	
			#ball.vel[1] = -ball.vel[1]
			#pad.pos[0] = pad.pos[0] - PAD_WIDTH/18
			None



	# Pad Buffers
	elif (ball.pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and ball.pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (ball.pos[0] >= pad.pos[0] - PAD_WIDTH/2 - math.fabs(ball.vel[0])*3 + pad.vel and ball.pos[0] <= pad.pos[0] - PAD_WIDTH/2):	# Hits Side of Pad Left
		ball.vel[0] = -ball.vel[0]
		ball.vel[1] = 5
		if debug == True:
			print("hit left")
	elif (ball.pos[1] >= pad.pos[1] - PAD_HEIGHT/2 and ball.pos[1] <= pad.pos[1] + PAD_HEIGHT/2) and (ball.pos[0] >= pad.pos[0] + PAD_WIDTH/2 and ball.pos[0] <= pad.pos[0] + PAD_WIDTH/2 + math.fabs(ball.vel[0])*3):	# Hits Side of Pad Left
		ball.vel[0] = -ball.vel[0]
		ball.vel[1] = 5
		if debug == True:
			print("hit right")
	
	# Brick Collision
	for brk in bricks:
		if (ball.pos[1] >= brk.pos[1] and ball.pos[1] <= brk.pos[1] + BRICK_HEIGHT):# and (ball.pos[0] >= brk.pos[0] and ball.pos[0] <= brk.pos[0] + BRICK_WIDTH):
			if ball.pos[0] >= brk.pos[0] and ball.pos[0] <= brk.pos[0] + 4: # LEFT
				ball.vel[0] = -ball.vel[0]
				brk.increase_hit()
				if brk.hit == brk.durability:
					bricks.remove(brk)
				break
			elif ball.pos[0] <= brk.pos[0] + BRICK_WIDTH and ball.pos[0] >= brk.pos[0] + BRICK_WIDTH - 4: # RIGHT
				ball.vel[0] = -ball.vel[0]
				brk.increase_hit()
				if brk.hit == brk.durability:
					bricks.remove(brk)
				break
		if (ball.pos[0] >= brk.pos[0] and ball.pos[0] <= brk.pos[0] + BRICK_WIDTH):
			if ball.pos[1] >= brk.pos[1] - 4 and ball.pos[1] <= brk.pos[1] + 4: # TOP
				brk.increase_hit()
				ball.vel[1] = -ball.vel[1]
				if brk.hit == brk.durability:
					bricks.remove(brk)
				break
			elif ball.pos[1] <= brk.pos[1] + BRICK_HEIGHT + 4 and ball.pos[1] >= brk.pos[1] + BRICK_HEIGHT - 4: # BOTTOM
				ball.vel[1] = -ball.vel[1]
				brk.increase_hit()
				if brk.hit == brk.durability:
					score += 100 * score_multi
					score_multi += 0.1
					print(score , score_multi)
					bricks.remove(brk)
				break
			#ball_init()
			#ball.vel[1] = -ball.vel[1]
			#break


	if debug == True:	
	#	for brk in bricks:
	#		print(brk.pos)
	#	pause(canvas)	
		None

	
	# Ball Death
	if ball.pos[1] >= HEIGHT:
		ball_init()
		pad.pos = [WIDTH/2, HEIGHT-HEIGHT/15]
		lives -= 1
		score_multi = 1
		if debug == True:
			print(lives)
			print("DEAD")
		



		# Hit box displays
	if debug == True:
		# Pad
		#pygame.draw.line(canvas, WHITE, [0, pad.pos[1] - PAD_HEIGHT/2], [WIDTH, pad.pos[1] - PAD_HEIGHT/2], 1) # Above
		#pygame.draw.line(canvas, WHITE, [0, pad.pos[1] + PAD_HEIGHT/2], [WIDTH, pad.pos[1] + PAD_HEIGHT/2], 1) # Bottom
		#pygame.draw.line(canvas, WHITE, [pad.pos[0] - PAD_WIDTH/2, 0], 	[pad.pos[0] - PAD_WIDTH/2, HEIGHT], 1) # Left Side
		#pygame.draw.line(canvas, WHITE, [pad.pos[0] + PAD_WIDTH/2, 0], 	[pad.pos[0] + PAD_WIDTH/2, HEIGHT], 1) # Right Side

		# Pad Buffer
		#pygame.draw.line(canvas, BLUE, 	[pad.pos[0] - PAD_WIDTH/2 - math.fabs(ball.vel[0])*3,0], [pad.pos[0] - PAD_WIDTH/2 - math.fabs(ball.vel[0])*3,HEIGHT] , 1) # Left
		#pygame.draw.line(canvas, BLUE, 	[pad.pos[0] + PAD_WIDTH/2 + math.fabs(ball.vel[0])*3,0], [pad.pos[0] + PAD_WIDTH/2 + math.fabs(ball.vel[0])*3,HEIGHT] , 1) # Right

		# Ball
		#pygame.draw.line(canvas, WHITE, [ball.pos[0], 0], [ball.pos[0], HEIGHT] , 1) # Vertical
		#pygame.draw.line(canvas, WHITE, [0, ball.pos[1]], [WIDTH, ball.pos[1]] , 1) # Horizontal

		# Bricks
		for brk in bricks:

			#pygame.draw.line(canvas, PURPLE, [brk.pos[0], 0], [brk.pos[0], HEIGHT] , 1) # left
			#pygame.draw.line(canvas, PURPLE, [brk.pos[0] + BRICK_WIDTH, 0], [brk.pos[0] + BRICK_WIDTH, HEIGHT] , 1) # right
			#pygame.draw.line(canvas, PURPLE, [0, brk.pos[1]], [WIDTH, brk.pos[1]], 1) # top
			#pygame.draw.line(canvas, PURPLE, [0, brk.pos[1] + BRICK_HEIGHT], [WIDTH, brk.pos[1] + BRICK_HEIGHT], 1) # bottom
			None





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
