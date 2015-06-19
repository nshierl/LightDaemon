import colorsys

class Rainbow:
	colorArray = []
	numLEDS = 0
	multiplier = 1

	def __init__(self, numLEDS, multiplier):
		self.multiplier = multiplier
		self.numLEDS = numLEDS * self.multiplier
		for i in range(0, self.numLEDS):
			self.colorArray.append(self.getRainbow(i))

	def getData(self):
		self.colorArray.append(self.colorArray.pop(0))
		return ''.join(self.colorArray[0::self.multiplier])

	def getRainbow(self, index):
		rgb = colorsys.hls_to_rgb((float(index) / self.numLEDS), .5, 1)
		return ''.join(chr(int(x * 255)) for x in rgb)
