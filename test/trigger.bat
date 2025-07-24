@echo off

@REM 기본값 - MOD_WORD: 0, MOD_TRIGGER: 1

set MOD_IP=172.30.1.77
set MOD_PORT=502
set MOD_WORD=0
set MOD_TRIGGER=1

python trigger.py --mod-ip %MOD_IP% --mod-port %MOD_PORT% --mod-word %MOD_WORD% --mod-trigger %MOD_TRIGGER%
