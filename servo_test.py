# Testing Servo (Model Power HD Standard Servo 3001HB

# Control of a servo via a Raspberry Pi is done using PWM (Pulse Wave Modulation)
# Typicaly most servo's expect a control signal of 50hz (50 cycles per second)
# The time we need to work with to control the servo using a 50hz control signal is calculated as 1 second / 50hz = 0.020 of a second or 20 milliseconds
# The position of the servo depends on the amount of time during a single cycle that the signal is switched on.
# Typically a servo will be fully left if the signal is on for 1 millisecond (note 1 millisecond equates to a duty cycle of 5% as 1 / 20 milliseconds = 0.05 or 5%). Duty cycle being the percentage of time the signal is switched on per cycle.
# Typically a servo will be in the middle if the signal is on for 1.5 milliseconds (note 1.5 milliseconds equates to a duty cycle of 7.5% as 1.5 / 20 milliseconds = 0.075 or 7.5%)
# Typically a servo will be in the fully right position if the sigbal is on for 2 milliseconds (note 2 milliseconds equates to a duty cycle of 10% as 2 / 20 milliseconds = 0.10 or 10%)
# Note these values can vary between servos so testing is needed to fully determine the correct values.
# In my testing i found the two values I needed were a duty cycle of 2.3% for fully left and a duty cycle of 10.9% for fully right.

# Servo leads are red for power (5v), brown for ground and orange for signal.

# For testing the servo power lead was connected to GPIO pin 2 (5v), the ground lead to GPIO pin 6 and the control/signal lead to GPIO pin 11.

# Import relevant libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO pinpoit mode to BOARD which numbers them sequencially.
GPIO.setmode(GPIO.BOARD)

# Setup GPIO pin 11 as the servo  control/signal pin
GPIO.setup(11, GPIO.OUT)

# Define pwm used to send control signals to the servo using PWM 
pwm = GPIO.PWM(11, 50)
# Start interaction with the servo and send to fully left position (duty cycle of 2.3%)
pwm.start(2.3)

# Test servo using a for loop to go fully right the left five times with a 2 second pause in between each movement
for i in range(5):
 # move fully right with a DC of 10.9%
 pwm.ChangeDutyCycle(10.9)
 time.sleep(2)
 # move fully left with a DC of 2.3%
 pwm.ChangeDutyCycle(2.3)
 time.sleep(2)

# Finally stop interaction with servo
pwm.stop()

# Cleanup/Reset GPIO pins before exiting
GPIO.cleanup()



