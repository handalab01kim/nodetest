# modbus_test_server.py
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock

def run_test_server():
    # Coil 0번에 초기값 False 설정
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*100),
        co=ModbusSequentialDataBlock(0, [0]*100),
        hr=ModbusSequentialDataBlock(0, [0]*100),
        ir=ModbusSequentialDataBlock(0, [0]*100),
    )
    context = ModbusServerContext(slaves=store, single=True)

    print("🧪 테스트용 Modbus 서버 실행 중 (port 5020)...")
    StartTcpServer(context, address=("localhost", 5020))

if __name__ == "__main__":
    run_test_server()
