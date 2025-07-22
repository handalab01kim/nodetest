Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\사용자이름\python-video-module"
WshShell.Run "cmd.exe /C python main.py --time 20 --mod-ip 172.30.1.77 --mod-port 502 --mod-word 0", 0, False
