@echo off
for /f "tokens=2 delims=," %%i in ('tasklist /FI "IMAGENAME eq python*" /FO CSV /NH') do (
    taskkill /F /PID %%i >nul 2>&1
)
@REM @echo off
@REM @REM 버전에 따른 python.exe 이름 확인 필요
@REM taskkill /F /IM python3.13.exe