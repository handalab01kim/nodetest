# USB 카메라에서 30fps로 프레임을 deque에 유지

import cv2
import time
from collections import deque
import threading

class CameraBuffer:
    def __init__(self, fps=30, seconds=20):
        self.fps = fps
        self.frame_size = None
        self.buffer_size = fps * seconds
        self.buffer = deque(maxlen=self.buffer_size)
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._capture_loop, daemon=True)
        self.thread.start()

    def _capture_loop(self):
        import logging
        logger = logging.getLogger("error_logger")
        while self.running:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("카메라 연결 실패")
                logger.info(f"카메라 연결 실패")
                # self.buffer.clear() # 카메라 연결 끊길 시 버퍼 제거?
                time.sleep(5)
                continue

            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # 1280*720
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 웹캠 해상도 불러오기
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.frame_size = (width, height)
            print(f"카메라 연결됨: {self.frame_size}")

            import logging
            logger = logging.getLogger("error_logger")
            logger.info(f"카메라 연결: {self.frame_size}")

            # c=0
            # timedebug=time.time()
            while self.running:
                ret, frame = cap.read()
                if not ret:
                    print("프레임 수신 실패")
                    logger.info("프레임 수신 실패")
                    break
                self.buffer.append(frame)
                # time.sleep(1 / self.fps) # opencv 자체 fps로 처리되기에 넣으면 지연되어 프레임이 1초 안에 30개 저장되지 못함. 저장 영상 재생 시 적은 프레임을 재생하기에 영상이 빨라 보이는 현상 발생
                # c+=1
                # if c==30:
                #     c=0
                #     print(time.time()-timedebug)
                #     timedebug=time.time()
            cap.release()

    def stop(self):
        self.running = False

    def get_frames(self):
        return list(self.buffer)

    def get_buffer_size(self):
        return self.buffer_size

    def get_frame_size(self):
        return self.frame_size

    def get_fps(self):
        return self.fps
