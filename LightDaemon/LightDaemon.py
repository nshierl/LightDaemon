import serial, os, time, sys, random, string, Tkinter
import spectrum, color

COM_PORT = 'COM3'
BAUD = 115200		# Fastest baud possible so speed up refresh
LED_COUNT = 110

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

	#dataClass = spectrum.SpectrumGenerator(LED_COUNT)	
	dataClass = color.Color(LED_COUNT, 0, 255, 100)
	while True:
		connection.write(dataClass.getData())
		time.sleep(0.05)

	l = Tkinter.Label(text = "See me?")
	l.pack()
	l.mainloop()


