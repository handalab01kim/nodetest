# for test

from pymodbus.client.sync import ModbusTcpClient
import time

client = ModbusTcpClient("172.30.1.77", port=502)

print("Trigger ON!!")
trigger_val = 1
client.write_register(0, trigger_val)

# time.sleep(1)
# print("Trigger OFF")
# client.write_coil(0, False)

client.close()
