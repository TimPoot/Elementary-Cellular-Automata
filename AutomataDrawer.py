from PIL import Image, ImageDraw
import math
import random

class AutomataDrawer:
	#takes the length of strip and the amount of iterations that the automata runs for
	def __init__(self, stripLength, iterations):
		self.stripLength = stripLength
		self.iterations = iterations
		self.canvas = Image.new("L", (1000, 1000))
		self.draw = ImageDraw.Draw(self.canvas)

		self.draw.rectangle([(0,0), (1000,1000)], 255)

		self.cellWidth = 25
		self.cellHeight = 25
		if (self.cellWidth * self.stripLength) > 1000:
			self.cellWidth = math.floor(1000 / self.stripLength)
		if (self.cellHeight * self.iterations) > 1000:
			self.cellHeight = math.floor(1000 / self.iterations)

	#draws one line from a strip (bitstring) and an offset for the height which is equal 
	#to the amount of iterations that have passed.  
	def drawLine(self, strip, offsetHeight):
		for index, cell in enumerate(strip):
			if cell:
				x0, y0 = index * self.cellWidth, offsetHeight * self.cellHeight
				x1, y1 = (index * self.cellWidth) + self.cellWidth, (offsetHeight * self.cellHeight) + self.cellHeight
				self.draw.rectangle([(x0, y0), (x1, y1)], 0)

	#takes the rule as string and saves the image as png with the rule as the filename
	def saveImage(self, rule):
		self.canvas.save(rule + ".png")