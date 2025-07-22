## dependencies
### 필수 패키지
pip install opencv-python pymodbus==2.5.3

### trigger: modbus->api 테스트 패키지
pip install fastapi uvicorn 


## run
```
python main.py --time 20
```

## test
```
python modbus_test_server.py
python modbus_test_write_trigger.py
```
