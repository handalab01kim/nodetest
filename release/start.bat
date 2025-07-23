@echo off
@REM config (TIME_: 영상 길이(초))
set TIME_=20
set MOD_IP=172.30.1.77
set MOD_PORT=502
set MOD_WORD=0

@REM 모듈 디렉토리 경로: 현재 디렉토리에서 실행 시 생략 가능
set PATH_="C:\Users\username\python-video-module"
cd %PATH_%

python main.py --time %TIME_% --mod-ip %MOD_IP% --mod-port %MOD_PORT% --mod-word %MOD_WORD%

pause