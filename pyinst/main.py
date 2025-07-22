from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import threading
import time
import sys
import subprocess
import os

program_mode = {"value": "A"}

def create_image():
    image = Image.new('RGB', (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, 56, 56), fill='blue')
    return image

def on_quit(icon, item):
    icon.stop()
    sys.exit(0)

def toggle_mode(icon, item):
    program_mode["value"] = "B" if program_mode["value"] == "A" else "A"
    print(f"[트레이] 모드 변경됨: {program_mode['value']}")

def open_console(icon, item):
    subprocess.Popen(["cmd.exe", "/k", "echo 로그 출력 창입니다. & pause"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def background_task():
    while True:
        print(f"[백그라운드] 현재 모드: {program_mode['value']}")
        time.sleep(5)

def main():
    t = threading.Thread(target=background_task, daemon=True)
    t.start()

    icon = Icon("TrayApp", create_image(), "My Tray App", menu=Menu(
        MenuItem("모드 변경", toggle_mode),
        MenuItem("로그 창 열기", open_console),
        MenuItem("종료", on_quit)
    ))
    icon.run()

if __name__ == "__main__":
    main()
