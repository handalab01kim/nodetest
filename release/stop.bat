@echo off
for /f "tokens=2 delims=," %%i in ('tasklist /FI "IMAGENAME eq python*" /FO CSV /NH') do (
    taskkill /F /PID %%i >nul 2>&1
)
