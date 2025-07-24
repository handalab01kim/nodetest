' ===== config =====
TIME_ = 20
MOD_IP = "172.30.1.77"
MOD_PORT = 502
MOD_WORD = 0
'PATH_ = "C:\Users\username\python-video-module"
PATH_ = "C:\Users\handa\repositories\nodejstest\release"

' ===== run =====
cmd = "python main.py" & _
      " --time " & TIME_ & _
      " --mod-ip " & MOD_IP & _
      " --mod-port " & MOD_PORT & _
      " --mod-word " & MOD_WORD

Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = PATH_
WshShell.Run "cmd.exe /C " & cmd, 0, False
