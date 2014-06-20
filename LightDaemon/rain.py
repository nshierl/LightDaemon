import random

DROPLET_COLOR = '\x00\xFF\xFF'

class Droplet:
	startIndex = 0
	currentIndex = 0
	direction = False # True - up | False - down
	ledHeight = 0

	def __init__(self, ledHeight, start, up):
		self.startIndex = start
		self.currentIndex = start
		self.direction = up
		self.ledHeight = ledHeight

	def getPosition(self):
		if (abs(self.startIndex - self.currentIndex) == self.ledHeight) or (self.currentIndex >= 109):
			return -1
		elif self.direction:
			self.currentIndex -= 1
			return self.currentIndex
		else:
			self.currentIndex += 1
			return self.currentIndex



class Rain:
	numLEDS = 0
	droplets = []
	data = []
	

	def __init__(self, numLEDS):
		self.numLEDS = numLEDS

	def getData(self):
		self.updateDroplets()
		self.createDroplets()
		return ''.join(self.data)

	def createDroplets(self):
		if random.randint(0, 20) % 7 == 0:
			self.droplets.append(Droplet(21, 50, True) if random.randint(0, 1) == 1 else Droplet(30, 80, False))

	def updateDroplets(self):
		self.data = ['\x00\x00\x00' for x in range(self.numLEDS)]
		for droplet in self.droplets:
			index = droplet.getPosition()
			if index == -1:
				self.droplets.remove(droplet)
			else:
				self.data[index] = DROPLET_COLOR

