@if "%1"=="" (
    start /b python main.py
) else (
    start /b python main.py --time %1
)
