# using port expander show raspberry pi CPU load using 8 LED's

import time, os, smbus

DEVICE = 0x20
IODIRA = 0x00
GPIOA = 0x12

bus = smbus.SMBus(1)
bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, GPIOA, 0x00)

while True:
	cpu1 = os.popen("vmstat 1 3").readlines()
	cpu2 = 2 ** int((100 - int(cpu1[4].split()[14])) * 0.08) -1
	bus.write_byte_data(DEVICE, GPIOA, cpu2)

	