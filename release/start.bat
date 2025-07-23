@echo off
@REM config (TIME: 영상 길이(초))
set TIME=20
set MOD_IP=172.30.1.77
set MOD_PORT=502
set MOD_WORD=0

python main.py --time %TIME% --mod-ip %MOD_IP% --mod-port %MOD_PORT% --mod-word %MOD_WORD%

pause