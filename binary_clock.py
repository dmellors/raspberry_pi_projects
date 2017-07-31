# Using a MCP23017 port expander to create a binary clock

# The hour is displayed using 4 LED's to represent the 4 bits needed to show the hour (8,4,2,1 gives a decimal range of 0-15)
# The minutes are displayed using six LED's to represent the six bits needed (32, 16, 8, 4,2, 1) gives a decimal range of 0-63)

import time, smbus

DEVICE = 0x20
IODIRA = 0x00
IODIRB = 0x01
GPIOA = 0x12
GPIOB = 0x13

bus = smbus.SMBus(1)
bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, IODIRB, 0x00)
bus.write_byte_data(DEVICE, GPIOA, 0x00)
bus.write_byte_data(DEVICE, GPIOB, 0x00)

m1 = 60

while True:
		current_time = time.localtime()
		minute = current_time.tm_min
		hour = current_time.tm_hour

		if hour > 12:
			hour = hour - 12
		if m1 <> minute:
			bus.write_byte_data(DEVICE, GPIOB, hour)
			bus.write_byte_data(DEVICE, GPIOA, minute)
		time.sleep(1)

