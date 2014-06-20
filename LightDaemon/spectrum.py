class SpectrumGenerator:
	numLEDS = 0
	rgbColor = [255,0,0]
	decrease = 0
	increase = 1
	index = 0

	def __init__(self, numLEDS):
		self.numLEDS = numLEDS

	def getData(self):
		self.increase = self.increase + 1 if self.rgbColor[self.increase] == 255 else self.increase
		self.increase = 0 if self.increase == 3 else self.increase
		self.decrease = self.decrease + 1 if self.rgbColor[self.decrease] == 0 else self.decrease
		self.decrease = 0 if self.decrease == 3 else self.decrease
		
		print "increase: %i decrease: %i r: %i g: %i b: %i " % (self.increase, self.decrease, self.rgbColor[0], self.rgbColor[1], self.rgbColor[2])

		self.rgbColor[self.decrease] -= 1
		self.rgbColor[self.increase] += 1
		self.index += 1
		return ''.join(chr(self.rgbColor[0])+chr(self.rgbColor[1])+chr(self.rgbColor[2]) for x in range(self.numLEDS))