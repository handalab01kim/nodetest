@echo off
chcp 65001 >nul

for /f "tokens=2 delims== " %%i in (
  'wmic process where "CommandLine like '%%video_recorder.py%%'" get ProcessId /value 2^>nul'
) do (
  echo 종료 중: PID %%i
  taskkill /PID %%i /F
)
pause