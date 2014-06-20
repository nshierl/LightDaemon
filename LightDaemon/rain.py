import random

class Droplet:
	startIndex = 0
	currentIndex = 0
	direction = False # True - up | False - down
	ledHeight = 0

	def __init__(self, ledHeight, start, up):
		self.startIndex = start
		self.direction = up
		self.ledHeight = ledHeight

	def getPosition(self):
		if abs(self.startIndex - self.currentIndex) == ledHeight:
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

	def __init__(self):
		pass

	def getData(self):
		pass

	def createDroplets(self):
		if random.randint(0, 20) == 10:
			self.droplets.append(Droplet(21, 50, True) if random.randint(0, 1) == 1 else Droplet(30, 80, False))

	def updateDroplets(self):
		for droplet in self.droplets:
			
