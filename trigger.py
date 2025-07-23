# for test

from pymodbus.client.sync import ModbusTcpClient
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mod-ip", type=str, default="localhost", help="Modbus 장치 IP")
parser.add_argument("--mod-port", type=int, default=5020, help="Modbus port")
parser.add_argument("--mod-word", type=int, default=0, help="Modbus word 주소")
parser.add_argument("--mod-trigger", type=int, default=0, help="Modbus trigger value")
args = parser.parse_args()

client = ModbusTcpClient(args.mod_ip, port=args.mod_port)

print("Trigger ON")
client.write_register(args.mod_word, args.mod_trigger)

client.close()
