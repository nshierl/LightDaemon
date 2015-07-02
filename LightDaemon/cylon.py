import math, time

class Cylon:

	color = [200,0,0]
	width = 7				#Use an odd number
	numLEDS = 0
	minIndex = 0
	maxIndex = 0
	middleIndex = 0
	frame = []
	eyeIndex = 0
	gamma = 1.3
	direction = 'left'
	multiplier = 1


	def __init__(self, numLEDS, minIndex, maxIndex, w = width, g = gamma, m = multiplier, col = color):
		self.numLEDS = numLEDS * m
		self.color = col
		self.width = w * m
		self.gamma = g
		self.multiplier = m
		self.minIndex = minIndex * m
		self.maxIndex = maxIndex * m
		self.middleIndex = int(((maxIndex - minIndex)/2)*m) 
		self.eyeIndex = self.middleIndex
		for x in range(self.numLEDS):
			self.frame.append('\x00\x00\x00')

	def eyeController(self):

		#test back and forth sweeping

		if self.direction == 'left' and self.eyeIndex <= self.maxIndex:
			self.moveEye(self.maxIndex)
			if self.eyeIndex == self.maxIndex:
				self.direction = 'right'
		
		if self.direction == 'right' and self.eyeIndex >= self.minIndex:
			self.moveEye(self.minIndex)
			if self.eyeIndex == self.minIndex:
				self.direction = 'left'

	def moveEye(self,newIndex):
		if newIndex == self.eyeIndex:
			return

		elif newIndex > self.eyeIndex:
			self.eyeIndex += 1

		else:
			self.eyeIndex -=1

	def getData(self):

		self.eyeController()

		offset = math.floor(float(self.width / 2))
		relativeIndex = int((self.eyeIndex - offset))

		for x in range(relativeIndex, relativeIndex+self.width):
			if x >= self.minIndex and x <= self.maxIndex:
				shading = float(abs(self.eyeIndex - x))
				shading = pow(shading/offset, (1.0/self.gamma))

				#print shading

				self.frame[x] = ''.join(chr(self.color[0] - int(self.color[0]*shading))+
					chr(self.color[1] - int(self.color[1]*shading))+
					chr(self.color[2] - int(self.color[2]*shading)))

		#cleanup
		if(relativeIndex - 1 >= self.minIndex):
			self.frame[relativeIndex - 1] = '\x00\x00\x00'

		if(relativeIndex + self.width + 1 < self.maxIndex):
			self.frame[relativeIndex + self.width + 1] = '\x00\x00\x00'

		return ''.join(self.frame[self.minIndex:self.maxIndex:self.multiplier])
		
