# trigger 들어오면 등록된 콜백(trigger_callback) 실행
from pymodbus.client.sync import ModbusTcpClient
from threading import Thread
import time

# 외부에서 등록되는 콜백 함수
trigger_callback = None

MODBUS_IP = "172.30.1.77"
MODBUS_PORT = 502
TRIGGER_REGISTER = 0   # Coil -> word 주소

def modbus_loop():
    client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
    client.connect()
    print(f"Modbus: {MODBUS_IP}:{MODBUS_PORT}")

    while True:
        try:
            # result = client.read_coils(TRIGGER_REGISTER, 1, unit=1)
            result = client.read_holding_registers(TRIGGER_REGISTER, 1, unit=1)
            if result and not result.isError():
                val = result.registers[0]
                print("modbus value:", val)
                if val :
                    print("Modbus 트리거 감지됨")
                    if trigger_callback:
                        Thread(target=trigger_callback).start()
            time.sleep(3)
        except Exception as e:
            print("Modbus 오류:", e)
            time.sleep(3)

def start():
    Thread(target=modbus_loop, daemon=True).start()
