' ===== config =====
' 모듈 디렉터리 경로 (한글 포함 X)
mainScriptPath = "C:\Users\username\python-video-module"
timeVal = 20
modIP = "172.30.1.77"
modPort = 502
modWord = 0

' ===== run =====
cmd = "python main.py" & _
      " --time " & timeVal & _
      " --mod-ip " & modIP & _
      " --mod-port " & modPort & _
      " --mod-word " & modWord

Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = mainScriptPath
WshShell.Run "cmd.exe /C " & cmd, 0, False

' 실행 확인용 foreground 실행 (WshShell.Run "cmd.exe /C " & cmd, 0, False 대신 실행)
' WshShell.Run "cmd.exe /C " & cmd &" & pause", 1, False