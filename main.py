import argparse
from camera_buffer import CameraBuffer
from trigger_handler import save_buffer_to_video
# import trigger_api
# import uvicorn
import trigger_modbus


# import argparse
# parser = argparse.ArgumentParser(description='time parser')
# parser.add_argument('--time', type=int, default=20, help='')
# config=parser.parse_args()
# buffer_time=config.time # --time 입력받은 값


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int, default=20, help="버퍼 유지 시간 (초)")
    args = parser.parse_args()

    # 카메라 버퍼 초기화
    cam = CameraBuffer(seconds=args.time)
    cam.start()

    # 트리거 콜백 함수 정의
    def on_trigger():
        frames = cam.get_frames()
        save_buffer_to_video(frames, cam.get_fps(), cam.get_frame_size())

    # 트리거 처리 함수 등록
    # trigger_api.trigger_callback = on_trigger
    trigger_modbus.trigger_callback = on_trigger

    # FastAPI 실행
    # print("🚀 FastAPI 서버 실행 중 (http://localhost:8000/trigger)")
    # uvicorn.run(trigger_api.app, host="0.0.0.0", port=8000)

    # modbus start
    trigger_modbus.start()


    # 프로그램 종료 방지 (무한 대기)
    import time
    print("📡 Modbus 트리거 대기 중... (종료하려면 Ctrl+C)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 종료합니다.")

if __name__ == "__main__":
    main()
