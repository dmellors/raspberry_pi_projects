import RPi.GPIO as GPIO
import time


# register the LCD display pin to RaspPi GPIO port mappings in below vars
LCD_RS = 25 # register select
LCD_E = 24 # enable (switching signal)
LCD_D4 = 23 # data bit 4
LCD_D5 = 17 # data bit 5
LCD_D6 = 27 # dat bit 6
LCD_D7 = 22 # data bit 7


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005


def lcd_enable():
	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

def lcd_byte(bits, mode):
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_D4, bits&0x10==0x10)
	GPIO.output(LCD_D5, bits&0x20==0x20)
	GPIO.output(LCD_D6, bits&0x40==0x40)
	GPIO.output(LCD_D7, bits&0x80==0x80)
	lcd_enable()
	GPIO.output(LCD_D4, bits&0x01==0x01)
	GPIO.output(LCD_D5, bits&0x02==0x02)
	GPIO.output(LCD_D6, bits&0x04==0x04)
	GPIO.output(LCD_D7, bits&0x08==0x08)
	lcd_enable()

def lcd_string(message):
	message = message.center(LCD_WIDTH, " ")
	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)

def lcd_display(z1, z2):
	lcd_byte(LCD_LINE_1, LCD_CMD)
	lcd_string(z1)
	lcd_byte(LCD_LINE_2, LCD_CMD)
	lcd_string(z2)

# Initialise display
lcd_byte(0x33,LCD_CMD) # 110011 Initialise
lcd_byte(0x32,LCD_CMD) # 110010 Initialise
lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
lcd_byte(0x01,LCD_CMD) # 000001 Clear display
time.sleep(E_DELAY)

try:
	while True:
		lcd_display("Biscuit", "")
		time.sleep(2.5)
		lcd_display("Loves his walks", "and gravy bones")
		time.sleep(2.5)
		lcd_display("But mostly loves", "Funcle Dan!")
		time.sleep(2.5)
except KeyboardInterrupt:
	GPIO.cleanup()
