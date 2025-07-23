' ===== 파라미터 설정 =====
' 모듈 디렉터리의 libs 경로
mainScriptPath = "C:\Users\사용자\python-video-module\libs"
timeVal = 20
modIP = "172.30.1.77"
modPort = 502
modWord = 0

' ===== 커맨드 =====
cmd = "python main.py" & _
      " --time " & timeVal & _
      " --mod-ip " & modIP & _
      " --mod-port " & modPort & _
      " --mod-word " & modWord

' ===== 실행 =====
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = mainScriptPath
WshShell.Run "cmd.exe /C " & cmd, 0, False

' foreground 실행
' WshShell.Run "cmd.exe /C " & cmd &" & pause", 1, False