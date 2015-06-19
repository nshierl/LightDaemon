import colorsys

class Rainbow:
	colorArray = []
	numLEDS = 0

	def __init__(self, numLEDS):
		self.numLEDS = numLEDS * 10
		for i in range(0, self.numLEDS):
			self.colorArray.append(self.getRainbow(i))


	def getData(self):
		self.colorArray.append(self.colorArray.pop(0))
		return ''.join(self.colorArray[0::10])

	def getRainbow(self, index):
		rgb = colorsys.hls_to_rgb((float(index) / self.numLEDS), .5, 1)
		return ''.join(chr(int(x * 255)) for x in rgb)
