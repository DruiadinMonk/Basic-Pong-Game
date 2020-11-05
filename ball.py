# Ball class for the game Pong.

# MODULES
import pygame



class Ball:

	# INITIALIZE
	def __init__(self, window, color, x, y, radius, vel_x, vel_y):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.radius = radius
		self.vel_x = vel_x
		self.vel_y = vel_y


	# DRAW BALL
	def drawBall(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

	# MOVE BALL
	def moveBall(self):
		self.x -= self.vel_x
		self.y -= self.vel_y
	
