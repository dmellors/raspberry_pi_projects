# Simulate a random dice roll with LED's

import RPi.GPIO as GPIO
import time
import random

# list containing LED GPIO pin numbers
LED = [18,23,24,25]
button = 7

# set GPIO mode of operation to BCM
GPIO.setmode(GPIO.BCM)

# disable GPIO warning events if pin already in use
GPIO.setwarnings(False)

# Initialise the operational state of each GPIO pin note button pin is set to IN as will recieve an input when button is pressed.
GPIO.setup(LED[0], GPIO.OUT, initial = 0)
GPIO.setup(LED[1], GPIO.OUT, initial = 0) 
GPIO.setup(LED[2], GPIO.OUT, initial = 0) 
GPIO.setup(LED[3], GPIO.OUT, initial = 0) 

GPIO.setup(button, GPIO.IN)

print ("Press the button to roll the dice!")
try:
	while True:
		# if button is pressed then:
		if GPIO.input(button) == 1:
			# first reset/turn off all LED's that were showing any previous result
			for x in range (4):
				GPIO.output(LED[x], 0)

			# Sleep for half a second to allow user to release button otherwise mulitple results are displayed.
			time.sleep(0.5)

			# Generate a random number between 1 and six if the button is pressed and display correct LED dice pattern 
			rolled_number = random.randrange(1,7)
			print ("You rolled a: ", rolled_number)
			print ("Press the button to roll dice again!")
			
			# Light up the appropiate LEDs to display the result
			# if a 1 is thrown
			if rolled_number == 1:
				GPIO.output(LED[1], 1)
			# if a 2 is thrown
			if rolled_number == 2:
				GPIO.output(LED[3], 1)
			# if a 3 is thrown
			if rolled_number == 3:
				GPIO.output(LED[1], 1)
				GPIO.output(LED[3], 1)
			# if a 4 is thrown
			if rolled_number == 4:
				GPIO.output(LED[0], 1)
				GPIO.output(LED[2], 1)
			# if a 5 is thrown
			if rolled_number == 5:
				GPIO.output(LED[0], 1)
				GPIO.output(LED[1], 1)
				GPIO.output(LED[2], 1)
			# if a 6 is thrown	
			if rolled_number == 6:
				GPIO.output(LED[0], 1)
				GPIO.output(LED[2], 1)
				GPIO.output(LED[3], 1)	


# if user exits program by pressing control-C then exit and reset all GPIO pins on the raspberry pi
except KeyboardInterrupt:
	GPIO.cleanup()