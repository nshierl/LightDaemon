class Color:
	color = [0, 0, 0]
	numLEDS = 0

	def __init__(self, numLEDS, r, g, b):
		self.color = [r, g, b]
		self.numLEDS = numLEDS

	def getData(self):
		return ''.join(chr(self.color[0])+chr(self.color[1])+
			chr(self.color[2]) for x in range(self.numLEDS))

	def setColor(self, r, g, b):
		self.color = [r, g, b]