import pyaudio
import wave
import sys
import numpy as np
import scipy
import colorsys

class AudioEqualizer:

	color = [255,0,0]

	CHUNK = 1024

	valNum = 255

	stream = None	

	valPerDoubling = 10.0
	threshold = 5

	decayConst = 0.9

	colorMode = 'Single'
	lightness = 0.5

	# binedges = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]
	# nbins = len(binedges) - 1
	# offsets = [0,0,0,0,0,0,0,0]

	binedges = [2,4,8,16,32,64, 128]
	nbins = len(binedges) - 1
	offsets = [-20,-14,-6,2,3,4]

	binval = 0.001 * np.ones(nbins, np.float)
	newbinval = np.zeros(nbins, np.float)

	minIndex = 0
	maxIndex = 0
	activeLEDs = 0

	ledPerBin = 0

	numLEDS = 0
	LEDS = []

	def __init__(self, numLEDS, minIndex, maxIndex, col = color, cm = colorMode, light = lightness):

		self.numLEDS = numLEDS
		self.minIndex = minIndex
		self.maxIndex = maxIndex
		self.activeLEDs = maxIndex - minIndex
		self.color = col
		self.colorMode = cm
		self.lightness = light

		self.ledPerBin = int((self.activeLEDs)/self.nbins)

		for x in range(numLEDS):
			self.LEDS.append('\x00\x00\x00')

		p = pyaudio.PyAudio()

		deviceInfo = p.get_default_input_device_info()

		print deviceInfo

		self.stream = p.open(channels = deviceInfo['maxInputChannels'],rate = int(deviceInfo['defaultSampleRate']),
						format = pyaudio.paInt16, input = True)

		print self.activeLEDs

	def getData(self):

		
		ret = ''

		data = self.stream.read(self.CHUNK)

		npdata = np.fromstring(data, dtype=np.int16)

		temp = []

		for x in xrange(self.CHUNK):
			temp.append((npdata[x*2]+npdata[x*2+1])/2)

		npProcessedData = np.array(temp)

		spectrum = np.abs(np.fft.fft(npProcessedData))

		for i in range(self.nbins):
			self.newbinval[i] = np.mean(spectrum[self.binedges[i]:self.binedges[i+1]])

		self.binval = np.maximum(self.newbinval, self.decayConst*self.binval)

		#print self.binval

		self.ledVal = np.maximum(0,np.round(np.maximum(0, np.minimum(self.valNum,
													self.valPerDoubling * np.log2(self.binval)
													+ self.offsets))) - self.valPerDoubling*self.threshold)

		#print self.ledVal
		if self.colorMode == 'Single':
			for x in range(0,self.activeLEDs):
				bin = (self.nbins - 1) - (x/self.ledPerBin)
				shade = self.ledVal[bin]/self.valNum
				self.LEDS[x + self.minIndex] = ''.join(chr(int(self.color[0]*shade))+
										chr(int(self.color[1]*shade))+
										chr(int(self.color[2]*shade)))
		if self.colorMode == 'Spectrum':
			for x in range(0,self.activeLEDs):
				bin = (self.nbins - 1) - (x/self.ledPerBin)
				shade = self.ledVal[bin]/self.valNum
				color = colorsys.hls_to_rgb(float(self.ledVal[bin]/255),self.lightness,1)

				self.LEDS[x+self.minIndex] = ''.join(chr(int(x*255*shade)) for x in color)
		#for x in range(0,self.numLEDS,self.ledPerBin):
			# for y in range(x,x+self.ledPerBin):
			# 	shade = self.ledVal[x/self.ledPerBin-1]/self.valNum
			# 	ret = (ret + chr(int(self.color[0] * shade)) + 
			# 			chr(int(self.color[1] * shade)) + 
			# 			chr(int(self.color[2] * shade)))

		return ''.join(self.LEDS[:])


		# print temp

		# print npProcessedData.size

		# print npProcessedData.shape
		# print npProcessedData.size
		# print npdata
		# print npProcessedData
