import argparse
from .camera_buffer import CameraBuffer
from .trigger_handler import save_buffer_to_video
from . import trigger_modbus

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int, default=20, help="영상 시간(초)")
    parser.add_argument("--mod-ip", type=str, default="localhost", help="Modbus 장치 IP")
    parser.add_argument("--mod-port", type=int, default=5020, help="Modbus port")
    parser.add_argument("--mod-word", type=int, default=0, help="Modbus word 주소")
    args = parser.parse_args()

    # 카메라 버퍼 초기화
    cam = CameraBuffer(seconds=args.time)
    cam.start()

    # 트리거 콜백 함수
    def on_trigger():
        frames = cam.get_frames()
        save_buffer_to_video(frames, cam.get_fps(), cam.get_frame_size())

    # args modbus 설정 전달
    trigger_modbus.configure(args.mod_ip, args.mod_port, args.mod_word)

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
