from pymodbus.client.sync import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=5020)

print("🚀 Trigger ON")
client.write_coil(0, True, unit=1)
time.sleep(1)
print("🔁 Trigger OFF")
client.write_coil(0, False, unit=1)

client.close()
