# python -m pyinstaller --onefile --noconsole main.py
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import time
import sys

def create_image():
    # 16x16 파란 원 아이콘
    image = Image.new('RGB', (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, 56, 56), fill='blue')
    return image

def on_quit(icon, item):
    icon.stop()
    sys.exit(0)

def background_task():
    while True:
        print("백그라운드 작업 중...")
        time.sleep(5)

def main():
    # 백그라운드 쓰레드 실행
    t = threading.Thread(target=background_task, daemon=True)
    t.start()

    # 트레이 아이콘 표시
    icon = Icon("TrayApp", create_image(), "My Tray App", menu=Menu(MenuItem("종료", on_quit)))
    icon.run()

if __name__ == "__main__":
    main()
