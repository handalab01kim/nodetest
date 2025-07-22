import argparse
from camera_buffer import CameraBuffer
from trigger_handler import save_buffer_to_video
import trigger_modbus

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int, default=20, help="버퍼 유지 시간 (초)")
    args = parser.parse_args()

    # 카메라 버퍼 초기화
    cam = CameraBuffer(seconds=args.time)
    cam.start()

    # 트리거 콜백 함수
    def on_trigger():
        frames = cam.get_frames()
        save_buffer_to_video(frames, cam.get_fps(), cam.get_frame_size())

    # 트리거 콜백 함수 등록
    trigger_modbus.trigger_callback = on_trigger
    trigger_modbus.start()


    # 프로그램 종료 X
    import time
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt: quit()

if __name__ == "__main__":
    main()
