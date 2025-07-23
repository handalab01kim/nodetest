@echo off
@REM config (TIME: 영상 길이(초))
set TIME=20
set MOD_IP=172.30.1.77
set MOD_PORT=502
set MOD_WORD=0

@REM 모듈 디렉토리 경로: 현재 디렉토리에서 실행 시 생략 가능
set DIRECTORY="C:\Users\username\python-video-module"
cd %DIRECTORY%

python main.py --time %TIME% --mod-ip %MOD_IP% --mod-port %MOD_PORT% --mod-word %MOD_WORD%

pause