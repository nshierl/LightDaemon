import colorsys

class SpectrumGenerator:
	numLEDS = 0
	currentHueIndex = 0
	maxHue = 10
	lightness = 0.5

	def __init__(self, numLEDS, multiplier, light = lightness):
		self.numLEDS = numLEDS
		self.lightness = light
		if(multiplier > 1):
			self.maxHue = self.maxHue * multiplier

	def getData(self):
		rgbColor = colorsys.hls_to_rgb((float(self.currentHueIndex) / (self.maxHue)), self.lightness, 1)

		self.currentHueIndex = self.currentHueIndex + 1
		if(self.currentHueIndex > self.maxHue):
			self.currentHueIndex = 0

		return ''.join(chr(int(rgbColor[0] * 255))+chr(int(rgbColor[1] * 255))+chr(int(rgbColor[2] * 255)) for x in range(self.numLEDS))
