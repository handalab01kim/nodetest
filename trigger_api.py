# 테스트용 모듈(모드버스 대신)
# POST /trigger 요청이 들어오면 등록된 콜백(trigger_callback)을 실행

from fastapi import FastAPI
from threading import Thread

app = FastAPI()
trigger_callback = None  # 외부에서 등록

@app.post("/trigger")
def trigger():
    if trigger_callback:
        Thread(target=trigger_callback).start()
        return {"status": "triggered"}
    else:
        return {"status": "no callback registered"}
