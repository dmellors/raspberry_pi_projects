import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

for i in range(30):
  for x in range (3):
    GPIO.output(25, 1)
    time.sleep(0.2)
    GPIO.output(25, 0)
    time.sleep(0.2)
  time.sleep(0.5)
  for y in range (3):
    GPIO.output(25, 1)
    time.sleep(0.7)
    GPIO.output(25, 0)
    time.sleep(0.7)
GPIO.cleanup()

