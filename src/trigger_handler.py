# 현재 버퍼 내용을 mp4로 저장
import cv2
import os
from datetime import datetime

def save_buffer_to_video(frames, fps, frame_size, output_dir="recordings", filename=None):
    if not frames:
        print("저장할 프레임 없음")
        return

    os.makedirs(output_dir, exist_ok=True)
    if filename==None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}.mp4"
    else:
        filename = filename + ".mp4"
    filepath = os.path.join(output_dir, filename)

    original_filename = filename[:-4]
    count=1
    while os.path.exists(filepath):
        filename = f"{original_filename} ({count}).mp4"
        filepath = os.path.join(output_dir, filename)
        count+=1

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filepath, fourcc, fps, frame_size)
    for frame in frames:
        out.write(frame)
    out.release()

    print(f"동영상 저장됨: {filepath}")
