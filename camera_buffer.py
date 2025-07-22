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
        while self.running:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("카메라 연결 실패")
                # self.buffer.clear() # 카메라 연결 끊길 시 버퍼 제거?
                time.sleep(5)
                continue

            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # 1280*720
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 웹캠 해상도 불러오기
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.frame_size = (width, height)
            print(f"카메라 연결: {self.frame_size}")

            while self.running:
                ret, frame = cap.read()
                if not ret:
                    print("프레임 수신 실패")
                    break
                self.buffer.append(frame)
                time.sleep(1 / self.fps)
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
