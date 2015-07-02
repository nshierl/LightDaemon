import serial, os, time, sys, random, string
import spectrum, color, rainbow, rain, time, cylon, audioEqualizer
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

COM_PORT = 'COM3'
BAUD = 250000		# Fastest baud possible so speed up refresh
LED_COUNT = 60

def init():
	connection = serial.Serial(COM_PORT, BAUD)
	time.sleep(1)
	sys.stdout.write('Waiting for Arduino to become ready')
	while not 'Ready' in connection.read(connection.inWaiting()):
		sys.stdout.write('.')
		time.sleep(0.1)
	print 'Ready'
	return connection

if __name__ == "__main__":
	connection = init()

	#init()
	#effectsList = {'Spectrum':lambda: spectrum.SpectrumGenerator(LED_COUNT, 200),
	#				'Color':lambda: color.Color(LED_COUNT, 0, 255, 100),
	#				'Rainbow':lambda: rainbow.Rainbow(LED_COUNT, 8),
	#				'Rain':lambda: rain.Rain(LED_COUNT)}

	#[effects.addItem(effect) for effect in effectsList.keys()]
	#dataClass = spectrum.SpectrumGenerator(LED_COUNT, 200, 0.1)
	#dataClass = color.Color(LED_COUNT, 1, 0, 0)
	#dataClass = rainbow.Rainbow(LED_COUNT, 8,0.1)
	#dataClass = rain.Rain(LED_COUNT)
	#dataClass = cylon.Cylon(LED_COUNT,0,LED_COUNT - 12,15,2.2,3)
	dataClass = audioEqualizer.AudioEqualizer(LED_COUNT,0, (LED_COUNT - 12),cm = 'Spectrum', light = 0.25)
	#app = QApplication(sys.argv)
	#w = QWidget()
	#w.setWindowTitle('Light Daemon')
	 
	# Set window size. 
	#w.resize(320, 150)
	 
	# Create ComboBox
	#effects = QComboBox(w)
	#effects.move(10,10)
	#[effects.addItem(effect) for effect in effectsList.keys()]

	
	# Show the window and run the app
	#w.show()
	#app.exec_()

	while True:
		data = dataClass.getData().ljust(LED_COUNT*3, '\x00')
		connection.write(data)
		time.sleep(0.01)
