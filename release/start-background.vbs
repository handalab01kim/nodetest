' WshShell.CurrentDirectory = mainScriptPath: 현재 디렉토리에서 실행 시 생략 가능
' mainScriptPath: 모듈 디렉터리 경로 (한글 포함 불가) / WshShell.CurrentDirectory 생략 시 사용하지 않음

' ===== config =====
timeVal = 20
modIP = "172.30.1.77"
modPort = 502
modWord = 0
mainScriptPath = "C:\Users\username\python-video-module"

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