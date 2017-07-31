import time, smbus

DEVICE = 0x20
IODIRA = 0x00
GPIOA = 0x12

bus = smbus.SMBus(1)
bus.write_byte_data(DEVICE, IODIRA, 0x00)
bus.write_byte_data(DEVICE, GPIOA, 0x00)

while True:
		j=1
		for i in range(8):
			bus.write_byte_data(DEVICE, GPIOA,j)
			j *= 2
			time.sleep(0.05)
