import spi

device_0 = spi.openSPI(device="/dev/spidev0.0")

to_send = [0x01]
# result = (0x00, 0x00, 0x00)
result = spi.transfer(device_0, tuple(to_send))


print("to send: %s" % str(to_send))
print("result: %s" % str(result))