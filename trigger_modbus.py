# trigger 들어오면 등록된 콜백(trigger_callback) 실행
from pymodbus.client.sync import ModbusTcpClient
from threading import Thread
import time

# 외부에서 등록되는 콜백 함수
trigger_callback = None

# 설정값 (필요 시 환경변수나 설정파일로 이동 가능)
MODBUS_IP = "127.0.0.1"
MODBUS_PORT = 5020
TRIGGER_REGISTER = 0  # Coil 주소 (예: 0번)
# MIN_INTERVAL = 12  # 최소 트리거 간격 (초)

def modbus_loop():
    client = ModbusTcpClient(MODBUS_IP, port=MODBUS_PORT)
    client.connect()
    print(f"📡 Modbus 연결됨: {MODBUS_IP}:{MODBUS_PORT}")

    while True:
        try:
            result = client.read_coils(TRIGGER_REGISTER, 1, unit=1)
            if result and not result.isError():
                coil = result.bits[0]
                if coil :
                    print("🎯 Modbus 트리거 감지됨")
                    if trigger_callback:
                        Thread(target=trigger_callback).start()
            time.sleep(1)
        except Exception as e:
            print("❌ Modbus 오류:", e)
            time.sleep(2)

def start():
    Thread(target=modbus_loop, daemon=True).start()
