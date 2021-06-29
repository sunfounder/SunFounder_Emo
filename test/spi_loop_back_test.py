import spidev

spi = spidev.SpiDev()
spi.open(0, 0)

to_send = [0x01]

result = spi.xfer2(list(to_send))
print("to send: %s" % to_send)
print("result: %s" % result)