
class paddle(object):

	def __init__(self, x, y, width, height, color):
		self.pos = [x,y]
		self.color = color
		self.vel = 0

 


class ball(object):

	def __init__(self, x, y, vel, radius, color):
		self.pos = [x,y]
		self.color = color
		self.radius = radius
		self.vel = vel

#	def __iter__(self):
#		return self

#	def next(self):
#		if 

