import os
import argparse
from .camera_buffer import CameraBuffer
from .trigger_handler import save_buffer_to_video
from . import trigger_modbus
from .error import error_log
import socket
import logging
logger = logging.getLogger("error_logger")

def occupy_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"{port} on!")
        return s
    except Exception as e:
        logger.exception(f"{port} 포트 점유 실패")
        print(f"{port} 포트 점유 실패")
        quit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int, default=20, help="영상 시간(초)")
    parser.add_argument("--mod-ip", type=str, default="localhost", help="Modbus 장치 IP")
    parser.add_argument("--mod-port", type=int, default=5020, help="Modbus port")
    parser.add_argument("--mod-word", type=int, default=0, help="Modbus word 주소")
    parser.add_argument("--txt-path", type=str, default="test.txt", help="저장할 영상 정보를 가진 txt 파일 경로")
    args = parser.parse_args()

    # 로거
    error_log(os.path.dirname(args.txt_path)) # txt와 같은 위치에 로그파일 저장

    # 서비스 시작 로그
    logger.info(f"서비스 시작;\ttime: {args.time},\ttxt_path: {args.txt_path}")

    # 카메라 버퍼 초기화
    cam = CameraBuffer(seconds=args.time)
    cam.start()

    # 트리거 콜백 함수
    def on_trigger(): # txt에서 동영상 저장 정보 조회
        # logger = logging.getLogger("error_logger")
        txt_args = None
        try:
            with open(args.txt_path, 'r') as f:
                info = f.readline()
                txt_args=[s.strip() for s in info.split(",")] # 공백 제거
                if len(txt_args)!=2:
                    # raise Exception("txt 파일 안에 ',' 기준 두 값이 존재해야 합니다.")
                    logger.exception("txt 파일 안에 ',' 기준 두 값이 존재해야 합니다.")
                    return
        except Exception as e:
            logger.exception(f"txt 파일 찾을 수 없음: {args.txt_path}")
            return  # 동영상 저장 로직만 종료
        # output_dir, filename = info.split(",")
        output_dir, filename = txt_args
        frames = cam.get_frames()
        save_buffer_to_video(frames, cam.get_fps(), cam.get_frame_size(), output_dir=output_dir, filename=filename)



    # args modbus 설정 전달
    trigger_modbus.configure(args.mod_ip, args.mod_port, args.mod_word)

    # 트리거 콜백 함수 등록
    trigger_modbus.trigger_callback = on_trigger
    trigger_modbus.start()


    # 포트 점유 - 중복 실행 X
    port=9988
    port_socket = occupy_port(port)

    # 프로그램 종료 X
    import time
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt: quit()
    

if __name__ == "__main__":
    main()
