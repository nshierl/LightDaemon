import random

DROPLET_COLOR = '\xFF\x00\x99'

#TODO Scale lighting for higher framerate

class Lightning:
	startIndex = 0
	stopIndex = 0
	initalIndex = 0
	index = 0

	def __init__(self, startIndex, stopIndex):
		self.startIndex = startIndex
		self.stopIndex = stopIndex

	def getLightningArray(self):
		ret = {}
		# Start lightning
		if random.randint(0, 100) % 99 == 0:
			self.initalIndex = random.randint(100, 200)
			self.index = self.initalIndex

		# Retrigger
		if (random.randint(0, 20) & 7 == 0) and (self.index != 0):
			self.index += int(self.index * random.random() * (1 - (self.index / self.initalIndex)))

		if self.initalIndex > 0:
			for index in range(self.startIndex, self.stopIndex):
				ret[str(index)] = ''.join([chr(int(255 * (self.index / self.initalIndex))) for x in range(0, 3)])
		self.index -= random.randint(0, int(self.index * .25)) if self.index > 0 else 0
		if self.index == 0:
			self.initalIndex = 0
		return ret


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
	lightning = None
	data = []


	def __init__(self, numLEDS):
		self.numLEDS = numLEDS
		self.lightning = Lightning(51, 80)

	def getData(self):
		lightningData = self.lightning.getLightningArray()
		self.updateDroplets()
		self.createDroplets()

		for key in lightningData:
			self.data[int(key)] = lightningData[key]

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
