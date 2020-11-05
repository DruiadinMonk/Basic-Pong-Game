# Paddle class for the game Pong.



# MODULES
import pygame



# CLASS
class Paddle:

	# INITALIZE
	def __init__(self, window, color, x, y, w, h):
		self.window = window
		self.color  = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	# DRAW PADDLES
	def drawPaddle(self):
		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h))
