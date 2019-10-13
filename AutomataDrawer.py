from PIL import Image, ImageDraw
import math

class AutomataDrawer:
	#takes the length of strip and the amount of iterations that the automata runs for
	def __init__(self, stripLength, iterations):
		self.stripLength = stripLength
		self.iterations = iterations
		self.canvas = Image.new("L", (1000, 1000))

		self.cellWidth = 10
		self.cellHeight = 10
		if (self.cellWidth * self.stripLength) > 1000:
			self.cellWidth = math.floor(1000 / self.stripLength)
		if (self.cellHeight * self.iterations) > 1000:
			self.cellHeight = math.floor(1000 / self.iterations)

		print("You now have a drawer with a stripLength of %s and a #iterations equal to %s !" % (self.stripLength, self.iterations))