# Simulate a traffic light with a pedestrian crossing using LED's

import RPi.GPIO as GPIO
import time

# For each LED store its position in the list traffic_lights below which references the appropiate GPIO pin for each LED, this makes it easier as can now simply refer to the variable name insread of specific GPIO pin number.
red = 0
yellow = 1
green = 2
pedestrian_red = 3
pedestrian_green = 4
button = 5

# list traffic_lights stores the real GPIO pin numbers for each LED
traffic_lights = [18,23,24,25,8,7]

# for example the red led on the traffic light can be refernced as traffic_lights[red] which is GPIO pin 18

# set GPIO mode of operation to BCM
GPIO.setmode(GPIO.BCM)

# disable GPIO warning events if pin already in use
GPIO.setwarnings(False)

# Initialise the operational state of each GPIO pin note button pin is set to IN as will recieve an input when button is pressed.
GPIO.setup(traffic_lights[red], GPIO.OUT, initial = 0) 
GPIO.setup(traffic_lights[yellow], GPIO.OUT, initial = 0)
GPIO.setup(traffic_lights[green], GPIO.OUT, initial = 1)
GPIO.setup(traffic_lights[pedestrian_red], GPIO.OUT, initial = 1)
GPIO.setup(traffic_lights[pedestrian_green], GPIO.OUT, initial = 0)
GPIO.setup(traffic_lights[button], GPIO.IN)

print ("Press the button to turn on the pedestrian light")

# loop until user presses control-C to exit
try:
	while True:
		# if button is pressed then:
		if GPIO.input(traffic_lights[button]) == 1:
			# Turn off green traffic light and turn on yellow traffic light and wait 1 second
			GPIO.output(traffic_lights[green], 0)
			GPIO.output(traffic_lights[yellow], 1)
			time.sleep(1)
			# Turn off yellow traffic light and turn on red traffic light and wait 1 second
			GPIO.output(traffic_lights[yellow], 0)
			GPIO.output(traffic_lights[red], 1)
			time.sleep(1)
			# Turn off Pedestrian crossing red light and turn on Pedestrian crossing green light and wait 4 seconds
			GPIO.output(traffic_lights[pedestrian_red], 0)
			GPIO.output(traffic_lights[pedestrian_green], 1)
			time.sleep(4)
			# Turn off pedestrian crossing green light and turn on pedestrian crossing red light and wait 1 second
			GPIO.output(traffic_lights[pedestrian_green], 0)
			GPIO.output(traffic_lights[pedestrian_red], 1)
			time.sleep(1)
			# Turn on traffic lights yellow light and wait one second
			GPIO.output(traffic_lights[yellow], 1)
			time.sleep(1)
			# Go back to normal so turn on traffic lights green light and turn of traffic lights yellow and red lights
			GPIO.output(traffic_lights[red], 0)
			GPIO.output(traffic_lights[yellow], 0)
			GPIO.output(traffic_lights[green], 1)
# if user exits program by pressing control-C then exit and reset all GPIO pins on the raspberry pi
except KeyboardInterrupt:
	GPIO.cleanup()
