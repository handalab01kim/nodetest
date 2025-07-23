' WshShell.CurrentDirectory = PATH_: 현재 디렉토리에서 실행 시 생략 가능
' PATH_: 모듈 디렉터리 경로 (한글 포함 불가) / WshShell.CurrentDirectory 생략 시 사용하지 않음

' ===== config =====
TIME_ = 20
MOD_IP = "172.30.1.77"
MOD_PORT = 502
MOD_WORD = 0
PATH_ = "C:\Users\username\python-video-module"

' ===== run =====
cmd = "python main.py" & _
      " --time " & TIME_ & _
      " --mod-ip " & MOD_IP & _
      " --mod-port " & MOD_PORT & _
      " --mod-word " & MOD_WORD

Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = PATH_
WshShell.Run "cmd.exe /C " & cmd, 0, False

' 실행 확인용 foreground 실행 (WshShell.Run "cmd.exe /C " & cmd, 0, False 대신 실행)
' WshShell.Run "cmd.exe /C " & cmd &" & pause", 1, False